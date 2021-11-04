import os
import psycopg2

DATABASE_URL = os.environ['postgres://fjzuswqhbulppy:0dc2dd4ed3fddc2621cd8b17325277d4f3dafc4c2d49a8632780655208f3da51@ec2-52-30-81-192.eu-west-1.compute.amazonaws.com:5432/dfb08l405ekte3']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')