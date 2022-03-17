#!/usr/bin/env python

from distutils.core import setup

setup(
    name='DBT-Cloud-Plugin',
    version='0.0.1',
    description='DBT Cloud Plugin for Apache Airflow',
    packages=[
        'dbt_cloud_plugin',
        'dbt_cloud_plugin.dbt_cloud',
        'dbt_cloud_plugin.hooks',
        'dbt_cloud_plugin.operators',
        'dbt_cloud_plugin.sensors',
    ],
)
