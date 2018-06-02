#将Django的默认数据库sqlite改为mysql
import pymysql
pymysql.install_as_MySQLdb()