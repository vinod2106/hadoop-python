import sys
from pyspark import SparkContext
import logging
class ComputeStats():
    
    def computeStatsForCollection(self,sc, countPerPartitions=100000, partitions=5):
        '''
        
        :param sc:
        :type sc:
        :param countPerPartitions:
        :type countPerPartitions:
        :param partitions:
        :type partitions:
        '''
        totalNumber = min(countPerPartitions * partitions, sys.maxsize)
        rdd = sc.parallelize(range(totalNumber), partitions)    
        return (rdd.mean(), rdd.variance())

    def quietLogs(self,sc):
        '''
        
        :param sc:
        :type sc:
        '''
        logger = sc._jvm.org.apache.log4j
        logger.LogManager.getLogger("org").setLevel(logger.Level.INFO)
        logger.LogManager.getLogger("akka").setLevel(logger.Level.INFO)
        return logger
        
if __name__ == "__main__":
    log = logging.getLogger(__name__)
    log.info("My test info statement")
    sc = SparkContext(appName="Hello Spark")
    print("Hello Spark Demo. Compute the mean and variance of a collection")
    cstats = ComputeStats()
    logger = cstats.quietLogs(sc)
    stats = cstats.computeStatsForCollection(sc);
    log.info("=======================>>> Results: ")
    log.info("=======================>>> Mean: " + str(stats[0]));
    log.info("========================>>> Variance: " + str(stats[1]));
    sc.stop()
