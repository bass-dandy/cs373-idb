all:
	adf

www:
	rm -rf /data/www
	mkdir -p /data/www
	cp -r static/* /data/www
