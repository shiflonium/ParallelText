.. _api:


***************
API
***************

This page will walk you through each method in **outfits > views.py** file. It contains pretty much the entire logic behind EZStyler.

.. _outfits-views:

Product Add with Image Processing
=================================
This is function gets called by ajax to add the product image to the outfit. 
In this Function we user image processing to remove the background of the image in the code below::
	print "pening file"
	img = backRemove(img)
	print "finishes prosessing"
		
	def dajax_save_product(request, id, url, title, price, sel_image):    
		if sel_image:
			if price != "Enter Product Price":
				price = price.strip('$')
				p = Product(
						title = title,
						price = price,
						url = url,
				)
			else:
				p = Product(
						title = title,
						url = url,
				)
				
			p.outfit_id = id
			
			image=sel_image
			
			if image [0] == "/":
				while image[0] == "/":
					image = image[1:]
				image = "http://" + image
				
			# r = requests.get(image)
			# print r
			# data = r.content
			# re = urllib.urlretrieve(image)
			# print re
			try:
				input_file = StringIO(urllib2.urlopen(image).read())
			except Exception,e: print str(e)
			
			output_file = StringIO()
			img = Image.open(input_file)
			
			######  Background Removal ######
			print "pening file"
			img = backRemove(img)
			print "finishes prosessing"
			
			img.thumbnail((300,300), Image.ANTIALIAS)
			img.save(output_file,"PNG")
			#img.save(output_file,"JPEG")

			#filename2 = urlparse(image).path.split('/')[-1]
			#print filename2
			#filename2 = filename2.replace ("-", "_")
			p.save()
			filename =  str(id)+"_"+str(p.id)+".png"
			p.images.save(filename, ContentFile(output_file.getvalue()), save=True)
			prod_id = p.outfit_id
			outfit = get_object_or_404(Outfit, pk=prod_id)
			action.send(request.user, verb='added product to ', action_object=p, target=outfit)        
			#action.send(request.user, verb='added product to ', action_object=outfit, target=p) 
			outfit = get_object_or_404(Outfit, pk=id)
			product = Product.objects.filter(outfit=id).order_by('-id')
			
			l=len(product)
			data64=range(0,l)
			i=0
			for p in product:
				file= "https://s3.amazonaws.com/ezstyler/" + str(p.images)
				#asset=urllib.urlopen(file).read().encode("base64").replace("\n", "")
				filetype = file.split('.')[-1]
				data_uri = urllib.urlopen(file).read().encode("base64").replace("\n", "")
				#img_tag = '<img alt="sample" src="data:image/jpeg;base64,{0}"/>'.format(data_uri)
				datauri = 'data:image/' + filetype + ';base64,' + data_uri
				data64[i]=datauri
				i=i+1

			product2=zip(product,data64)
			product_form = ProductForm()
			canvas = outfit.canvas2

			protable = render_to_string('outfits/dajax_product_list.html',
			{'products': product2,
				'outfits': outfit,
				'canvas': canvas,
				'product_form':product_form,
				}, context_instance=RequestContext(request))
			#print protable

			return simplejson.dumps({'protable':protable})
	dajaxice_functions.register(dajax_save_product)
	
Outfit Details (with similar outfits)
=======================================
The code below is what renders the page with the outfit details as well as calls the function to generate similar outfits.
More detailed implimentation of machine learning algorithims can be viewed in the next section.::

	@login_required
	def outfit_detail(request, id):
		"""This view is renders the outfit_detail template with a list of all the 
		products associated with that outfit's id."""
		
		outfit = get_object_or_404(Outfit, pk=id)
		product = Product.objects.filter(outfit=id).values('title','url','images')
		#comments = Comment.objects.filter(object_pk=outfit.pk).order_by('submit_date')
		#length = len(comments)
		#outfit_form = OutfitForm(instance=outfit)
		#outfit_form.fields['collection'].queryset = Collection.objects.filter(author=request.user).order_by('-pk')
		user_outfits = Outfit.objects.filter(author=outfit.author_id)[:4]
		rating_ids=[]
		i=0
		ratings = RatedItem.objects.filter(user=request.user).values('object_id', 'score')
		for rating in ratings:
			rating_ids.append(rating['object_id'])
			i=i+1
		
		#calculate_similar_items(RatedItem.objects.all(), 4)
		sim = outfit.rating.similar_items()[:4].fetch_generic_relations()
		#sim = SimilarItem.objects.filter(content_type=27).filter(object_id=id)[:4].fetch_generic_relations()
	 
		
		return render_to_response('outfits/outfit_detail.html',
		{'products': product,
			'outfits': outfit,
			'user_outfits': user_outfits,
			'sim_outfits':sim,
			'ids':rating_ids,
			'ratings':ratings,
			}, context_instance=RequestContext(request))
			
Image Processing
==================
The following code consists of all the code designed for skin and background removal from product images. ::

	import cv2
	from cv2 import cv
	import Image
	import numpy
	import pymeanshift as pms

	minimumSize = (20, 20)
	mininumNeighbors = 2
	#imageScale = 2
	haar_scale = 1.2
	haar_flags = 0

	class ImageProcess:
		
		# sourceImage: PIL format
		# get skin mask image
		def getSkinMask(self, sourceImage):
			#img = cv2.imread(sourceImage)
			img = cv2.cvtColor(numpy.asarray(sourceImage), cv2.COLOR_RGB2BGR)
			omin = numpy.array([0, 58, 89], numpy.uint8)
			omax = numpy.array([25, 173, 229], numpy.uint8)
			hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			threshed = cv2.inRange(hsv, omin, omax)
			return Image.fromarray(threshed)
		
		# return meanshift segmented image as numpy array type
		def meanshift(self, img, spatial_radius=6, range_radius=15, min_density=1000):
			(segmented_image, labels_image, number_regions) = pms.segment(img, spatial_radius=spatial_radius,
																		  range_radius=range_radius, min_density=min_density)
			#Image.fromarray(segmented_image).save('cache.png')
			return segmented_image

		# detect face, and return face region
		def isFaceFound(self, img, cascade=cv.Load('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')):
			CV_Image = cv.LoadImageM(img, cv.CV_LOAD_IMAGE_COLOR)
			PIL_Image = Image.fromstring("RGB", cv.GetSize(CV_Image), CV_Image.tostring())
			CVImageHeader = cv.CreateImageHeader(PIL_Image.size, cv.IPL_DEPTH_8U, 3)
			cv.SetData(CVImageHeader, PIL_Image.tostring())
			imageWidth, imageHeight = Image.open(img).size
			grayScaleImage = cv.CreateImage((imageWidth,imageHeight), 8, 1)
			cv.CvtColor(CV_Image, grayScaleImage, cv.CV_BGR2GRAY)
			faces = cv.HaarDetectObjects(CV_Image, cascade, cv.CreateMemStorage(0), haar_scale, mininumNeighbors, haar_flags, minimumSize)
			face_region = []
			if faces:
				for ((x,y,w,h),n) in faces:
					cvPoint1 = (int(x), int(y))
					cvPoint2 = (int(x + w), int(y + h))
					cv.Rectangle(CV_Image, cvPoint1, cvPoint2, cv.RGB(255, 0, 0), 3, 8, 0)
					face_region.append((cvPoint1, cvPoint2))
			found = False
			if faces: found = True
			else: face_region = [((0, 0), (0, 0))]
			#cv.ShowImage("CV_Image", CV_Image)
			return found, face_region[0]

		# get body seed only if face is found
		def getBodySeed(self, face_region):
			face_left = face_region[0]
			face_right = face_region[1]
			#print face_left, face_right
			# approsimate body width is +/- half the face width from left/right face
			half_face = (face_right[0] - face_left[0]) / 2.0
			body_left = (int(face_left[0] - half_face), int(face_right[1] + (half_face / 2.0)))
			body_right = (int(face_right[0] + half_face), int((face_right[1] + half_face) * 2.5))

			row_width = body_right[0] + body_left[0]
			row_height = body_right[1] + body_left[1]

			seed = (row_width/2, row_height/2)
			return seed

		def canny(self, sourceImage, noiseScale=(5, 5), aSize=3):
			#if os.path.exists(sourceImage):
			# read the source image
			#img = cv2.imread(sourceImage)
			# convert to gray scale
			imgGrayScale = cv2.cvtColor(sourceImage, cv2.COLOR_BGR2GRAY)
			# use gaussian blur to reduce image noise,
			# higher noiseScale reduce more noise/detail
			imgGassianBlur = cv2.GaussianBlur(imgGrayScale, noiseScale, 0)

			edgeDetected = cv2.Canny(imgGassianBlur, 0, 50, apertureSize=aSize)
			#edgeDetected2 = cv2.Canny(imgGassianBlur, 0, 50, apertureSize=aSize)
			#kernel = numpy.ones((2,2),'uint8')
			#cv2.dilate(edgeDetected, kernel, dst=edgeDetected2)
			#cv2.imwrite('edged.jpg', edgeDetected)
			#cv2.imwrite('edged2.jpg', edgeDetected2)
			return edgeDetected

		# sourceImage: PIL format
		# maskImage: PIL format, postprocessed image
		# remove target rgba value from source image
		def removePixelByMask(self, sourceImage, maskImage, targetRGBA=(0, 0, 0, 0)):
			maskRGBA = maskImage.convert('RGBA')
			maskData = maskRGBA.getdata()
			mask_data_array = []
			for pixel in maskData:
				if targetRGBA == pixel:
					mask_data_array.append(0)
				else: mask_data_array.append(1)

			sourceRGBA = sourceImage.convert('RGBA')
			sourceData = sourceRGBA.getdata()
			new_source_data = []
			index = 0
			for pixel in sourceData:
				if mask_data_array[index] == 0: new_source_data.append((0, 0, 0, 0))
				else: new_source_data.append(pixel)
				index += 1
			sourceRGBA.putdata(new_source_data)
			return sourceRGBA
			

		def removeBackgroundByRegion(self, sourceImage, regionGrowingImage, colorRGB=150):
			regionImage = Image.open(regionGrowingImage)
			width, height = regionImage.size
			imgRGBA = regionImage.convert('RGBA')
			imgData = imgRGBA.getdata()
			x = y = 0
			main_array = []
			for item in imgData:
				x += 1
				if item[0] > colorRGB  and item[1] > colorRGB and item[2] > colorRGB:
					main_array.append(1)
				else:
					main_array.append(0)

			pic = Image.open(sourceImage)
			picRGBA = pic.convert('RGBA')
			picData = picRGBA.getdata()
			index = 0
			new_data = []
			for item in picData:
				if main_array[index] == 0:
					new_data.append((0, 0, 0, 0))
				else:
					new_data.append(item)
				index += 1
			picRGBA.putdata(new_data)
			return picRGBA

		# sourceImage: PIL format
		# edgeDetectedImage: PIL format, postprocessed image
		# scanBy: 0 = scan by horizontal, 1 = scan by vertical
		# smartMode: only useful after removeBackgroundByScan run at least once.
		#            ex: removeBackgroundByScan(img1, img2, 1)
		#                removeBackgroundByScan(img1, img2, 0, smartMode=True)
		# colorRGB: color range is background color that distingush from edge color
		def removeBackgroundByScan(self, sourceImage, edgeDetectedImage, face_size=0, scanBy=0, smartMode=False, colorRGB=20):
			rotation = 0
			if scanBy == 1:
				rotation = 90
			imgRGBA = edgeDetectedImage.rotate(rotation).convert('RGBA')
			imgDatas = imgRGBA.getdata()
			width, height = imgRGBA.size
			x = y = 0
			main_array = []
			sub_array = []

			pic = sourceImage.rotate(rotation)
			picRGBA = pic.convert('RGBA')
			picDatas = picRGBA.getdata()

			for imgData in imgDatas:
				x += 1
				if imgData[0] > colorRGB  and imgData[1] > colorRGB and imgData[2] > colorRGB:
					sub_array.append(1)
				else:
					sub_array.append(0)
				if x == width:
					try:
						left_index = sub_array.index(1)
						right_index = width - 1
						while sub_array[right_index] != 1:
							right_index -= 1
						right_index += 1
						left_background = sub_array[:left_index]
						right_background = sub_array[right_index:]
						mid_object = [1] * (right_index - left_index)
						row = left_background + mid_object + right_background
						if smartMode:
							while left_index < right_index and (right_index - left_index) > face_size:
								if picRGBA.getpixel((left_index, y)) == (0, 0, 0, 0):
									end = left_index
									while imgRGBA.getpixel((end, y)) < (20, 20, 20, 255):
										end += 1
									#if end >= width: break
									while imgRGBA.getpixel((left_index, y)) < (20, 20, 20, 255):
										left_index -= 1
									row_left = row[:left_index]
									row_right = row[end:]
									row = row_left + [0] * (end - left_index) + row_right
									left_index = end
								else:
									left_index += 1
						main_array.extend(row)
					except ValueError:
						main_array.extend([0] * width)
					x = 0
					y += 1
					sub_array = []
			index = 0
			new_data = []
			for picData in picDatas:
				if main_array[index] == 0:
					new_data.append((0, 0, 0, 0))
				else:
					new_data.append(picData)
				index += 1
			picRGBA.putdata(new_data)
			return picRGBA.rotate(-1 * rotation)

		def regionGrowing(self, sourceImage, seed, threshold=50):
			img = cv2.cv.LoadImage(sourceImage, cv2.cv.CV_LOAD_IMAGE_GRAYSCALE)
			img_size = cv2.cv.GetSize(img)
			region = cv2.cv.CreateImage(img_size, cv2.cv.IPL_DEPTH_8U, 1)
			cv2.cv.Zero(region)

			contour = []
			contour_value = []
			size = 1
			distance = 0
			
			region_mean = float(img[seed[1], seed[0]])
			pixel_area = img_size[0] * img_size[1]
			
			LEFT = (-1, 0)
			RIGHT = (1, 0)
			TOP = (0, 1)
			DOWN = (0, -1)
			LEFT_TOP = (-1, 1)
			RIGHT_TOP = (1, 1)
			LEFT_DOWN = (-1, -1)
			RIGHT_DOWN = (1, -1)
			#orientation = [RIGHT, TOP, LEFT, DOWN]
			orientation = [LEFT, RIGHT, TOP, DOWN, LEFT_TOP, LEFT_DOWN, RIGHT_TOP, RIGHT_DOWN]
			current_pixel = [seed[0], seed[1]]

			while(pixel_area > size and threshold > distance):
				for i in range(4):
					temp_pixel = [current_pixel[0] + orientation[i][0], current_pixel[1] + orientation[i][1]]

					if img_size[0] > temp_pixel[0] > 0 and img_size[1] > temp_pixel[1] > 0:
						is_in_img = True
					else:
						is_in_img = False
							
					if (is_in_img and (region[temp_pixel[1], temp_pixel[0]] == 0)):
						contour.append(temp_pixel)
						contour_value.append(img[temp_pixel[1], temp_pixel[0]] )
						region[temp_pixel[1], temp_pixel[0]] = 150
			
				distance = abs(int(numpy.mean(contour_value)) - region_mean)

				distance_list = [abs(i - region_mean) for i in contour_value ]
				distance = min(distance_list)
				index = distance_list.index(min(distance_list))
				region[current_pixel[1], current_pixel[0]] = 255
				size += 1
					
				region_mean = (size * region_mean + float(contour_value[index])) / (size+1)
				current_pixel = contour[index]

				del contour[index]
				del contour_value[index]

			return region


			
Suggestions 
============
The code below is all the functions used for calculation of users and similar outfits. ::


	from math import sqrt

	import django
	from django.contrib.auth.models import User
	from django.contrib.contenttypes.generic import GenericForeignKey
	from django.contrib.contenttypes.models import ContentType
	from django.db import connection

	def get_content_object_field(rating_model):
		opts = rating_model._meta
		for virtual_field in opts.virtual_fields:
			if virtual_field.name == 'content_object':
				return virtual_field # break out early
		return opts.get_field('content_object')

	def is_gfk(content_field):
		return isinstance(content_field, GenericForeignKey)

	def query_has_where(query):
		if django.VERSION < (1, 2):
			return query.where.as_sql()[0] is None
		else:
			qn = connection.ops.quote_name
			return query.where.as_sql(qn, connection)[0] is None

	def query_as_sql(query):
		if django.VERSION < (1, 2):
			return query.as_sql()
		else:
			return query.get_compiler(connection=connection).as_sql()

	def sim_euclidean_distance(ratings_queryset, factor_a, factor_b):
		rating_model = ratings_queryset.model
		
		if isinstance(factor_a, User):
			filter_field = 'user_id'
			match_on = 'hashed'
			lookup_a = factor_a.pk
			lookup_b = factor_b.pk
		else:
			filter_field = 'hashed'
			match_on = 'user_id'
			lookup_a = rating_model(content_object=factor_a).generate_hash()
			lookup_b = rating_model(content_object=factor_b).generate_hash()

		sql = """
		SELECT r1.score - r2.score AS diff
		FROM
			%(ratings_table)s AS r1
		INNER JOIN
			%(ratings_table)s AS r2
		ON r1.%(match_on)s = r2.%(match_on)s
		WHERE
			r1.%(filter_field)s = '%(lookup_a)s' AND
			r2.%(filter_field)s = '%(lookup_b)s'
			%(queryset_filter)s
		"""
		
		rating_query = ratings_queryset.values_list('pk').query
		if query_has_where(rating_query):
			queryset_filter = ''
		else:
			q, p = query_as_sql(rating_query)
			rating_qs_sql = q % p
			queryset_filter = ' AND r1.id IN (%s)' % rating_qs_sql
		
		params = {
			'ratings_table': rating_model._meta.db_table,
			'filter_field': filter_field,
			'match_on': match_on,
			'lookup_a': lookup_a,
			'lookup_b': lookup_b,
			'queryset_filter': queryset_filter
		}

		cursor = connection.cursor()
		cursor.execute(sql % params)
		
		sum_of_squares = 0
		while True:
			result = cursor.fetchone()
			if result is None:
				break
			sum_of_squares += result[0] ** 2
		
		return 1 / (1 + sum_of_squares)

	def sim_pearson_correlation(ratings_queryset, factor_a, factor_b):
		rating_model = ratings_queryset.model
		qn = connection.ops.quote_name
		
		if isinstance(factor_a, User):
			filter_field = 'user_id'
			match_on = 'hashed'
			lookup_a = factor_a.pk
			lookup_b = factor_b.pk
		else:
			filter_field = 'hashed'
			match_on = 'user_id'
			lookup_a = rating_model(content_object=factor_a).generate_hash()
			lookup_b = rating_model(content_object=factor_b).generate_hash()

		sql = """
		SELECT 
			SUM(r1.score) AS r1_sum, 
			SUM(r2.score) AS r2_sum, 
			SUM(r1.score*r1.score) AS r1_square_sum, 
			SUM(r2.score*r2.score) AS r2_square_sum,
			SUM(r1.score*r2.score) AS p_sum,
			COUNT(r1.id) AS sample_size
		FROM
			%(ratings_table)s AS r1
		INNER JOIN
			%(ratings_table)s AS r2
		ON r1.%(match_on)s = r2.%(match_on)s
		WHERE
			r1.%(filter_field)s = '%(lookup_a)s' AND
			r2.%(filter_field)s = '%(lookup_b)s'
			%(queryset_filter)s
		"""
		
		rating_query = ratings_queryset.values_list('pk').query
		if query_has_where(rating_query):
			queryset_filter = ''
		else:
			q, p = query_as_sql(rating_query)
			rating_qs_sql = q % p
			queryset_filter = ' AND r1.id IN (%s)' % rating_qs_sql
		
		params = {
			'ratings_table': rating_model._meta.db_table,
			'filter_field': filter_field,
			'match_on': match_on,
			'lookup_a': lookup_a,
			'lookup_b': lookup_b,
			'queryset_filter': queryset_filter
		}

		cursor = connection.cursor()
		cursor.execute(sql % params)

		result = cursor.fetchone()

		if not result:
			return 0

		sum1, sum2, sum1_sq, sum2_sq, psum, sample_size = result

		if sum1 is None or sum2 is None or sample_size == 0:
			return 0
		
		num = psum - (sum1 * sum2 / sample_size)
		den = sqrt((sum1_sq - pow(sum1, 2) / sample_size) * (sum2_sq - pow(sum2, 2) / sample_size))
		
		if den == 0:
			return 0
		
		return num / den

	def top_matches(ratings_queryset, items, item, n=5, 
					similarity=sim_pearson_correlation):
		scores = [
			(similarity(ratings_queryset, item, other), other)
				for other in items if other != item]
		scores.sort()
		scores.reverse()
		return scores[:n]

	def recommendations(ratings_queryset, people, person,
						similarity=sim_pearson_correlation):
		rating_model = ratings_queryset.model
		
		already_rated = ratings_queryset.filter(user=person).values_list('hashed')
		
		totals = {}
		sim_sums = {}
		
		for other in people:
			if other == person:
				continue
			
			sim = similarity(ratings_queryset, person, other)
			
			if sim <= 0:
				continue
			
			# now, score the items person hasn't rated yet
			for item in ratings_queryset.filter(user=other).exclude(hashed__in=already_rated):
				totals.setdefault(item.content_object, 0)
				totals[item.content_object] += (item.score * sim)
				
				sim_sums.setdefault(item.content_object, 0)
				sim_sums[item.content_object] += sim
		
		rankings = [(total / sim_sums[pk], pk) for pk, total in totals.iteritems()]
		
		rankings.sort()
		rankings.reverse()
		return rankings

	def calculate_similar_items(ratings_queryset, num=10):
		# get distinct items from the ratings queryset - this can be optimized
		field = get_content_object_field(ratings_queryset.model)

		if is_gfk(field):
			rated_ctypes = ratings_queryset.values_list('content_type', flat=True).distinct()
			ctypes = ContentType.objects.filter(pk__in=rated_ctypes)
			for ctype in ctypes:
				ratings_subset = ratings_queryset.filter(content_type=ctype)
				rating_ids = ratings_subset.values_list('object_id')
				queryset = ctype.model_class()._default_manager.filter(pk__in=rating_ids)
				_store_top_matches(ratings_queryset, queryset, num, True)
		else:
			rated_model = field.rel.to
			rating_ids = ratings_queryset.values_list('content_object__pk')
			queryset = rated_model._default_manager.filter(pk__in=rating_ids)
			_store_top_matches(ratings_queryset, queryset, num, False)
			
	def _store_top_matches(ratings_queryset, rated_queryset, num, is_gfk):
		from ratings.models import SimilarItem
		
		ctype = ContentType.objects.get_for_model(rated_queryset.model)
		rated_pks = rated_queryset.values_list('pk')
		
		for item in rated_queryset.iterator():
			matches = top_matches(ratings_queryset, rated_queryset, item, num)
			for (score, match) in matches:
				si, created = SimilarItem.objects.get_or_create(
					content_type=ctype,
					object_id=item.pk,
					similar_content_type=ContentType.objects.get_for_model(match),
					similar_object_id=match.pk)
				if created or si.score != score:
					si.score = score
					si.save()

	def recommended_items(ratings_queryset, user):
		from ratings.models import SimilarItem
		scores = {}
		total_sim = {}

		for item in ratings_queryset.filter(user=user):
			
			for similar_item in SimilarItem.objects.get_for_item(item.content_object):
			
				actual = similar_item.similar_object
				lookup_kwargs = ratings_queryset.model.lookup_kwargs(actual)
				lookup_kwargs['user'] = user
				
				if ratings_queryset.filter(**lookup_kwargs):
					continue
				
				scores.setdefault(actual, 0)
				scores[actual] += similar_item.score * item.score
				
				total_sim.setdefault(actual, 0)
				total_sim[actual] += similar_item.score
		
		rankings = [(score/total_sim[item], item) for item, score in scores.iteritems()]
		
		rankings.sort()
		rankings.reverse()
		return rankings

outfits_list
============
Displays the list of outfits. It uses *classic* generic views to display the page.

Outfits are filtered by the user that is currently logged in. In other words - display outfits that belong to their respective owner::

  @login_required
  def outfit_list(request):
      outfits = Outfit.objects.filter(author=request.user).order_by('name')
      return render(request, 'outfits/outfit_list.html', {'outfits': outfits})

outfits_detail
==============

Detailed page of the outfit includes product's image, title, price, link to the original website and the HTML5 canvas to drag and drop products onto::

  @login_required
  def outfit_detail(request, id):
      add_product_form = AddProductForm()

      if request.method == "POST":
          if add_product_form.is_valid():
              product_form = ProductForm(request.POST)
              return render(request, 'outfits/product_add.html', {
                  'product_form': product_form
              })
          else:
              print 'invalid'
              outfit = get_object_or_404(Outfit, pk=id)
              return render(request, 'outfits/outfit_detail.html', {
                  'add_product_form': add_product_form,
                  'outfits': outfit
              })
      else:
          outfit = get_object_or_404(Outfit, pk=id)
          product = Product.objects.filter(outfit=id)
          canvas = outfit.canvas
          return render_to_response('outfits/outfit_detail.html',
          {'products': product,
              'outfits': outfit,
              'canvas': canvas
              }, context_instance=RequestContext(request))
              
outfits_create
==============

Creates an empty outfit. On GET, the user will see a form with a
textfield and a submit button. When the button is clicked, the form is
validated against the database. First we try to check for any object 
belonging to that user with the outfit name sepecified. If no Exceptions 
occur the outfit create page is reloaded and a message that "Nmae is 
already being used" is displayed to the user. The exception of 
MultipleObjectsReturned should never be raised but if it does we do the 
same thing. Only if the ObjectDoesNotExist exception is raised should 
the outfit be created with the specified name. Then the method save(commit=False) 
has to be passed in order to save the User ID who created that outfit. That way
each outfit is associated only to the user who created it. Finally,
on success it redirects a user back to the list of outfits. Also this 
view can recieve a post from the javascript Modal "outfit_list" page::
              
  @login_required
  def outfit_create(request):
      if request.method == "POST":
          outfit_form = OutfitForm(request.user, request.POST)
          if outfit_form.is_valid():
              name2 = request.POST['name']
              AllOutfits = Outfit.objects.filter(author=request.user)

              try:
                  AllOutfits = AllOutfits.get(name=name2)
                  outfit_form = OutfitForm()
                  return render(request, 'outfits/outfit_create.html', {'outfit_form': outfit_form, 'message': 'name is already used'})
              except MultipleObjectsReturned:
                  outfit_form = OutfitForm()
                  return render(request, 'outfits/outfit_create.html', {'outfit_form': outfit_form, 'message': 'name is already used'})        
              except ObjectDoesNotExist:
                  outfit = outfit_form.save(commit=False)
                  outfit.author = request.user
                  outfit.save()
                  id = outfit.id
                  return redirect(outfit_detail, id)
      else:
          outfit_form = OutfitForm()
          return render(request, 'outfits/outfit_create.html', {'outfit_form': outfit_form})


product_delete
==============

Passes the otufit id of product and the product id to the delet_object() Generic View. The object is then deleted and post_delete_redirect to oufit_detail page::

  @login_required
  def product_delete(request, id, pid):
      return delete_object(request,
          model=Product,
          object_id=pid,
          template_name='outfits/product_delete.html',
          template_object_name='products',
          post_delete_redirect=reverse('outfit_detail', args=[id]))

product_update
==============

Retrieve the product specified by the outfit id and product id using 
get_object_or_404. Then send the product url, title and product to the 
template. These values will be in the ProductForm The use can make changes 
and submit. On POST the view saves the POSTed values to the corisponding 
product object. Then it will redirect back to the outfit_details page::

  @login_required
  def product_update(request, id, pid):
      product = get_object_or_404(Product, pk=pid)
      url=product.url
      title=product.title
      if request.method == 'POST':
          product_form = ProductForm(request.POST, instance=product)
          if product_form.is_valid():
              product = product_form.save(commit=False)
              product.save()
              return redirect(outfit_detail, id)
      else:
          product_form = ProductForm(instance=product)
          return render(request, 'outfits/product_update.html', {
          'product_form': product_form, 'url':url, 'title':title, 'p':product })

product_add
===========

If this view is called withoput a POST then render the AddProductForm on the 
product_add template. Ususlay this view will be called with a POST by a submited 
form from a javascript Modal Reveal on the outfit_detail page. The view then checks 
that the POST is a URL. if it is, it is opened using urllib2.urlopen(url).read(). 
Then it passed to BeautifulSoup so we can begin to scrape and extract data. The 
first thing we extract is the page "Title" by looking for the title tag. Next we 
search for sever formats of displaying a price, most important is the "$" sign.
If no price is found we display "Enter a Price" in the ProductForm instead. 
Next we search for all <img> tags. we then extract the "src" attribute of each one 
and save it to a list. We then use ImageParser() to read only a few bits at a time 
from each image header until the image dimensions are determined. Once we determine 
the demensions we stop reading the rest of the file. We then use the dimensions to 
check the conditions if the width and hight must me greater than 200px and the 
ratio of h/w and w/h must me less than 3. This is done to minimize the amount 
of irrelevant images displayed to the user. Each image that meets these requirements 
is added to the BigImg list. Then the Title, Price, and BigImg list is saved in a 
session and is redirected to the product_confirm view to render the next page::

  @login_required
  def product_add(request, id):
      if request.method == "POST":
          add_product_form = AddProductForm(request.POST)
          if add_product_form.is_valid():
              url = add_product_form.cleaned_data['url']
              webpage = urllib2.urlopen(url).read()
              soup = BeautifulSoup(webpage)

              title = soup.head.title.string
              priceRE1 = re.compile('(\$\d*\.\d{2})')
              priceRE2 = re.compile('(\$\d*\,\d{3})')
              priceRE3 = re.compile('(\$\d*\,\d{3}\.\d{2})')
              priceRE4 = re.compile('(\$\s\d*\.\d{2})')
              priceRE5 = re.compile('(\$\s\d*\,\d{3}\.\d{2})')

              findPatPrice = re.findall(priceRE1, webpage)
              findPatPrice += re.findall(priceRE2, webpage)
              findPatPrice += re.findall(priceRE3, webpage)
              findPatPrice += re.findall(priceRE4, webpage)
              findPatPrice += re.findall(priceRE5, webpage)

              p = len(findPatPrice)
              try:
                  price = findPatPrice[p - 1]
              except:
                  price = "Enter Product Price:"

              allImg = soup.findAll('img')#,{'src' : re.compile(r'(jpe?g)|(jp?g)|(png)|(tif)')})
              l = len(allImg)
              i = 0
              image_list = range(0, l)

              for link2 in allImg:
                  image_list[i] = link2.get('src')
                  i = i + 1

              i = 0
              BigImg = range(0, l)
              #y=len(image_list)
              formlist=["GIF","BMP"]
              for img2 in image_list:
                  try:
                      img_file = urllib2.urlopen(img2)
                  except:
                      try:
                          img_file = urllib2.urlopen('http://' + img2)
                      except:
                          img_file = urllib2.urlopen('http://www.gorell.com/images/colors-white-icon.jpg')
  ###################### Try reading only file header ####################                
                  #im = cStringIO.StringIO(img_file.read())
                  try:
                      p = ImageFile.Parser()
                      while 1:
                          data = img_file.read(300)
                          if not data:
                              break
                          p.feed(data)
                          if p.image:
                              # im_format=p.image.format
                              # if im_format in formlist:
                                  # break
                              # else:
                              print 'i am in if p.image'
                              w = p.image.size[0]
                              h = p.image.size[1]
                              if (w > 200 and 200< h < (w+w+w)) or (h > 200 and 200< w < (h+h+h)):
                                  print 'i am in if w>200 and 200<h'
                              # if (w > 200) and (h > 200):
                                  # print p.image.size
                                  # ratio1 = w / h
                                  # ratio2 = h / w
                                  # if(ratio1 < 3.0 and ratio2 < 3.0):
                                      # BigImg[i] = img2
                                      # i = i + 1
                                      
                                  BigImg[i] = img2
                                  i = i + 1
                              break
                      img_file.close()
  ########################################################################                
                  # im = cStringIO.StringIO(img_file.read())
                  # try:
                      # image = Image.open(im)
                  except:pass
                      # img_file = urllib2.urlopen('http://www.gorell.com/images/colors-white-icon.jpg')
                      # im = cStringIO.StringIO(img_file.read())
                      # image = Image.open(im)
                      # w = image.size[0]
                      # h = image.size[1]
                      # ratio1 = w / h
                      # ratio2 = h / w

              image_list = BigImg[0:i]

              request.session['product'] = {
                  'url': url,
                  'title': title,
                  'price': price,
                  'images': image_list
              }
              return redirect(product_confirm, id)
      else:
          add_product_form = AddProductForm()
          return render(request, 'outfits/product_add.html', {
              'add_product_form': add_product_form
          })


product_confirm
===============

The form starts out with a data stored by the session from the previous
View - product_add. The session data contains all required information:
title, price, url and images list. Notice images are not passed into the
product_form when product_form loads, instead they are rendered manually
in the product_confirm.html template. The reason for creating a form with
scraped data is to let the user verify that price and name are indeed
correct. On POST (user selected an image) the form is submitted to the 
save_product_redirect view with the selected image data::

  @login_required
  def product_confirm(request, id):
      product = request.session.get('product')
      image_list = product['images']
      title = product['title']
      price = product['price']
      url = product['url']
      
      price = price.strip('$')
      
      return render_to_response('outfits/product_confirm.html',
          {'id': id,
          'title': title,
          'url':url,
          'price': price,
          'image_list': image_list}, context_instance=RequestContext(request))
    
    
save_product
============

On POST (user selected an image) the form is saved right away after assigning an
outfit.id. The image processing and saving is done last. We run a background 
removal algorithm that reads the first byte pixel of the slected image, assumes 
that the color of that pixel is the background color and removes all pixels with 
that color within a certain threshold. Then the requests library gives the content 
method to store binary data of an image in memory. The filename is exactly the 
same as the original image filename. And finally it is saved into the database by 
calling save method on images field of the Product model and passing both filename 
and file as arguments. Then the page is redirected to the outfit_detail page::

  def save_product_redirect(request,id):
      if 'sel_image' in request.POST:
          image=request.POST['sel_image']
      if 'price' in request.POST:
          price=request.POST['price']
      if 'title' in request.POST:
          title=request.POST['title']
      if 'id' in request.POST:
          id=request.POST['id']
      if 'url' in request.POST:
          url=request.POST['url']
          
      
      #if request.method == 'POST':
      price = price.strip('$')

      Product.objects.all()
      p = Product(
              title = title,
              price = price,
              url = url,
      )
      #if product_form.is_valid():
      #p = product.save(commit=False)
      p.outfit_id = id
      p.save()

      r = requests.get(image)
      data = r.content

      img_temp = NamedTemporaryFile()
      img_temp.write(data)
      img_temp.flush()

      filename = urlparse(image).path.split('/')[-1]
      p.images.save(filename, File(img_temp), save=True)
      
      ##################  remove image background ################
      entry = p.images
      img_temp2 = NamedTemporaryFile()
      img_temp2.write(removeBG.removeBG(entry, scale=30))
      img_temp2.flush()
      p.images.save(filename, File(img_temp2), save=True)
      #############################################################

      return redirect(outfit_detail, id)
      # else:
          # product_form = ProductForm({
              # 'title': title,
              # 'price': price,
              # 'url': image,
          # })
          # return render(request, "outfits/product_confirm.html", {
              # 'product_form': product_form,
              # 'images': image,
          # })


outfit_update
=============

Functions the same as the product_update view::

  @login_required
  def outfit_update(request, id):
      outfit = get_object_or_404(Outfit, pk=id)
      if request.method == 'POST':
          outfit_form = OutfitForm(request.user, request.POST, instance=outfit)
          if outfit_form.is_valid():
              outfit = outfit_form.save(commit=False)
              outfit.save()
              return redirect(outfit_detail, id)
      else:
          outfit_form = OutfitForm(instance=outfit)
      return render(request, 'outfits/outfit_update.html', {
          'outfit_form': outfit_form
      })

outfit_delete
=============

Functions the same as the product_delete view

  @login_required
  def outfit_delete(request, id):
      return delete_object(request,
          model=Outfit,
          object_id=id,
          template_name='outfits/outfit_delete.html',
          template_object_name='outfit',
          post_delete_redirect=reverse("outfit_list")
      )


outfit_saveCanvas
=================

This view is called on submission of JSON canvas data and image datauri (which are 
both generated byt javascript on the page) from the outfit_detail page. The JSON 
data is the canvas configuration at the time of submission. The image dataURI is 
a snapshot of the canvas formated as a png. The function checks if the POSTed 
values are valid. The canvas JSON is saved in the Outfit.canvas field. Then we need 
to save the snapshot dataURI to a thumbnail to be viewed on the outfit_list page. To 
do this we run some functions to convert from a dataURI in base64 to a saved png file. 
This file is then saved using same method we used to save the product image via an 
ImageField() in Outfit.thumb. We also required to overwrite the previous thumbnail 
file if it existed. To do this we overwrite the object save() function to check if 
the filename exists, the file should be deleted then the new file should be writen. 
This new save() function can be seen in the Outfit model. Once all the saving has 
completed we redirect back to the outfit_detail page::

  @login_required
  def outfit_saveCanvas(request, id): 
      outfit = get_object_or_404(Outfit, pk=id)

      if request.method == 'POST':
          if 'canvas' in request.POST:
              canvas = request.POST['canvas']
              datauri = request.POST['thumb']
              outfit.canvas = canvas
              #outfit.save()
              user=outfit.author
              name=outfit.name
              e = str(outfit.thumb1)
              if e == "0":
                  outfit.thumb1 = "1"
              elif e == "1":
                  outfit.thumb1 = "0"
              else:
                  outfit.thumb1 = "0"
  ###########original thumbnail attempt################################################3
              #thumbimg = "static/" + str(outfit.thumb)
             
              # Create a Python file object using open()
              #thumb2 = open(filename, 'wb')
              #thumb = File(thumb2)
  ##################################################################################3####    
          
              filename = str(user) + "_" + str(name) + ".png"
              imgstr = re.search(r'base64,(.*)', datauri).group(1)
              img_temp = NamedTemporaryFile()
              img_temp.write(imgstr.decode('base64'))
              img_temp.flush()
              
  ########tried to make model for thumbnail so when i delete model object the image will be deleted also############
              #pics = get_object_or_404(OutfitThumb, name=filename)
              # try:
                  # print "deleted"
                  # pics = get_object_or_404(OutfitThumb, name=filename)
                  # pics.delete()
              # except: pass
              
              # pics = OutfitThumb(name=filename,)
              # pics.outfit_id = id
              # pics.save()
  ##################################################################################################################
              print outfit.thumb1
              #filename = urlparse(image).path.split('/')[-1]
              outfit.thumb.save(filename, File(img_temp), save=True)
      return redirect(outfit_detail, id)

    


