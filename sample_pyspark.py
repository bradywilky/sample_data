from pyspark.sql.functions import when, col
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',2500)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]

df = spark.createDataFrame(data=data, schema = columns)

df.withColumn("salary_band", when(col("salary_band") > 3000, "band_A").otherwise("band_B"))

df.show()
----------------------------------------------------------------------------------------------------------------


# 1) Explain what each line of code is doing
# 2) What is the resulting output of the last line of code?
