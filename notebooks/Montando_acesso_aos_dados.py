# Databricks notebook source
# MAGIC %scala
# MAGIC dbutils.fs.mkdirs("/mnt/dados")

# COMMAND ----------

display(dbutils.fs.ls("/mnt"))

# COMMAND ----------

# MAGIC %scala
# MAGIC val configs = Map(
# MAGIC   "fs.azure.account.auth.type" -> "OAuth",
# MAGIC   "fs.azure.account.oauth.provider.type" -> "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
# MAGIC   "fs.azure.account.oauth2.client.id" -> "509e3d5b-ed0b-44f5-86b8-a425235dc873",
# MAGIC   "fs.azure.account.oauth2.client.secret" -> "_rF8Q~Se96AhsgLCG3JKSXutOCKUCll_6f5zha7G",
# MAGIC   "fs.azure.account.oauth2.client.endpoint" -> "https://login.microsoftonline.com/51cdcaa4-8bf9-4d5c-9d66-b806ec7c4fdc/oauth2/token")
# MAGIC // Optionally, you can add <directory-name> to the source URI of your mount point.
# MAGIC dbutils.fs.mount(
# MAGIC   source = "abfss://imoveis@datalakealura.dfs.core.windows.net/",
# MAGIC   mountPoint = "/mnt/dados",
# MAGIC   extraConfigs = configs)
# MAGIC

# COMMAND ----------

display(dbutils.fs.ls("/mnt/dados"))

# COMMAND ----------


