from pyspark.sql import SparkSession

class Customer():
    
    #create context
    # Initiate Spark Session
    spark = SparkSession.builder.appName("PySpark WholeSaleCustomers").getOrCreate()
    sparkDF = spark.read.csv("D:\dev\git\hadoop-python\src\main\resources\WholesaleCustomersData.csv", header = True)
    sparkDF
    
if __name__ == '__main__':
    pass
