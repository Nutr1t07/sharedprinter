import logging
import sys
from queue import Queue
from threading import Thread
from orderManager.Linker_http import Linker
from orderManager.orderProcessor import OrderProcessor

server = "https://wwkserver.top/wwkserver/"
deviceID = 2
orderList = "orderList/"
messageQueue = Queue(maxsize=0)

if __name__ == "__main__":
	logging.basicConfig(
		level = logging.INFO,
		format = '[%(asctime)s] [%(levelname)s] (%(funcName)s) %(message)s',
		stream = sys.stdout
	)
	logger = logging.getLogger("priner")
	logger.info("Start printer!")
	myOrderProcessor = OrderProcessor(orderList, messageQueue)
	myLinker = Linker(server, deviceID, myOrderProcessor, messageQueue)
	Thread(target=myLinker.checkloop).start()
	Thread(target=myOrderProcessor.processOrders).start()
