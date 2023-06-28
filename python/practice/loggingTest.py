import logging


def foo():
    logging.basicConfig(
        format='{"l":"%(levelname)s" "t":"%(asctime)s" %(pathname)s.%(lineno)d msg:%(message)s}',
        level=logging.DEBUG,
        datefmt='%Y/%m/%d %H:%I:%S%z',
        encoding='utf-8'
    )

    logging.warning("Sample debug message %s", "testmessage")


foo()
