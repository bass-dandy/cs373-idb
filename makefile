all:
	adf

www:
	rm -rf /data/www
	mkdir -p /data/www
	cp -r static/* /data/www

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  Tests.tmp
	rm -rf __pycache__

test: Tests.tmp

Tests.tmp: tests.py
	#python3 tests.py > Tests.tmp 2>&1
	coverage3 run --branch tests.py >  Tests.tmp 2>&1
	coverage3 report -m              >> Tests.tmp
	cat Tests.tmp