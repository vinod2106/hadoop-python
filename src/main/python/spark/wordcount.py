from __future__ import print_function

from operator import add
from pyspark.sql import SparkSession
from utils.utils import Utils
# create logger

class WordCount():
    
  
    sc = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()
        
    
    log4jLogger = sc._jvm.org.apache.log4j
    logger = log4jLogger.LogManager.getLogger("PySpark")
    #logger.setLevel('INFO')
    
    
    logger.info(" ############## pyspark script logger initialized #############")
    
    print(logger.handlers)
    
    ostype = Utils.getPlatform()
    logger.info('ostype dir ====>'+ ostype)
    inputFile = "D://dev//git//hadoop-python//src//main//resources//input.txt"
    
    dir = Utils.GetFilePath(inputFile)
    logger.info('dir ====>'+ dir)
    
    lines = sc.read.text(inputFile).rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    sc.stop()
    
if __name__ == "__main__":
    pass
