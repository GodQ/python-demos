# -*- coding: utf-8 -*-
from pymongo import MongoClient
import gridfs
import os


class MongoOperator(object):
    def __init__(self, url, db_name="autorunner", replicaset=None):
        self._client = MongoClient(url, connect=False,
                                   replicaset=replicaset)
        self._db_name = db_name
        self._db = None
        self._fs = None
        self._switch_db(self._db_name)

    def __enter__(self):
        self._switch_db(self._db_name)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.close()

    @property
    def client(self):
        return self._client

    @property
    def db(self):
        return self._db

    @property
    def fs(self):
        if not self._fs:
            self._fs = gridfs.GridFS(self._db, collection='autorunner_fs')

        return self._fs

    def add_file_to_mongo(self, file_path, target_path, **kwargs):
        with open(file_path, "r+b") as f:
            self.fs.put(f, filename=target_path, **kwargs)

    def _switch_db(self, db_name):
        self._db = self._client[db_name]
        self._fs = None

        return self._db


MONGO_SETTINGS = {
    "url": "mongodb://autorunner:htq08_6s6e0EMi2@172.29.10.50:18038,172.29.10.70:18038,172.29.10.201:18038/autorunner?authMechanism=SCRAM-SHA-1",
    "db_name": "autorunner",
    "replicaset": 'rs001'}

if __name__ == '__main__':
    opt = MongoOperator(**MONGO_SETTINGS)

    # file_id = "772_1537172303_4162543.log"
    file_id = "675_1536749249_4653487_43127074-13dd-3dd2-9f43-69c0d0b98f3f_result_python3.zip"
    target_dir = "../tmp/"

    with opt as o:
        client = o.client
        db = o.db
        fs = o.fs
        fd = fs.get(file_id)
        data = fd.read()
        target_path = os.path.join(target_dir, file_id)
        with open(target_path, "wb") as tfd:
            tfd.write(data)



