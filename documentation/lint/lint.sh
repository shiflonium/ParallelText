pylint ../../manage.py ../../home/*py ../../pt_main/*py > ADMIN_LINT
pylint ../../ptext/*py > LIRON_LINT
pylint ../../parallel_display/*py > YONATAN_LINT
pylint ../../register/*.py ../../login/*py > KEVIN_LINT
pylint ../../manage.py ../../home/*py ../../pt_main/*py  ../../ptext/*py  ../../parallel_display/*py  ../../register/*.py ../../login/*py > GLOBAL_LINT
rm *LINT~
grep "Your code has been rated" *LINT
