# -*- coding:utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True


class CompanyConfig(Config):

    @classmethod
    def sql(cls):
        SQL_HOST = "192.168.152.130"
        SQL_PORT = "3306"
        SQL_USER = "root"
        SQL_PASSWD = "Ipad20180611"
        return [SQL_USER,SQL_PASSWD,SQL_HOST,SQL_PORT]


class HomeConfig(Config):

    @classmethod
    def sql(cls):
        DEBUG = True
        SQL_HOST = "192.168.152.130"
        SQL_PORT = "3306"
        SQL_USER = "root"
        SQL_PASSWD = "Ipad20180611"
        return [SQL_USER,SQL_PASSWD,SQL_HOST,SQL_PORT]

config = {
	"company_config":CompanyConfig,
	"home_config":HomeConfig
}

if __name__=="__main__":
	print(config['company_config'].sql())