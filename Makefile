all:
	$(shell cd Learcode; ./bootstrap; ./configure --with-blitz=/usr/lib64/blitz; make;)
	$(shell cp Learcode/app/dump_rhog .;)

clean:
	rm -f dump_rhog
	$(shell cd Learcode; git clean -fd)
