# Databricks notebook source
print("Hello world")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello world from sql!"

# COMMAND ----------

# MAGIC %md
# MAGIC # title1
# MAGIC ## title 2
# MAGIC ### title 3

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')
print(files)

# COMMAND ----------

display(files)
