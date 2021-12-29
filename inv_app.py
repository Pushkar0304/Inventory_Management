# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 13:13:53 2021

@author: Pushkar Patil
"""

from flask import Flask,render_template,request,redirect
import pymysql

inv_app = Flask(__name__)

@inv_app.route('/')
def dashboard():
    try:
        db = pymysql.connect(host="localhost",user="root",password="",db="inv_management")
        cu = db.cursor()
        sql = "select * from product_details"
        cu.execute(sql)
        data = cu.fetchall()
        return render_template('inv_dashboard.html',details=data)
    
    except Exception:
        return "Connection failed !!"

@inv_app.route('/add')
def form():
    return render_template('add_product.html')

@inv_app.route('/insert' , methods=['POST','GET'])
def insert():
    pn = request.form['name']
    pr = request.form['price']
    qty = request.form['quantity']
    dt = request.form['date']
    
    #return pn+pr+qty+dt
    try:
        db = pymysql.connect(host="localhost",user="root",password="",db="inv_management")
        cu =db.cursor() 
        sql="insert into product_details(name,price,quantity,date)values('{}','{}','{}','{}')".format(pn,pr,qty,dt)
        cu.execute(sql) 
        db.commit() 
        return redirect('/') 
    except Exception:
        return "Connection Failed !!"
    
@inv_app.route('/delete/<rid>')
def delete(rid):
    try:
        db = pymysql.connect(host="localhost",user="root",password="",db="inv_management")
        cu = db.cursor()
        sql = "delete from product_details where id='{}'".format(rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception:
        return "Connection failed !!"

@inv_app.route('/edit/<rid>')
def edit(rid):
    try:
        db = pymysql.connect(host="localhost",user="root",password="",db="inv_management")
        cu = db.cursor()
        sql = "select * from product_details where id='{}'".format(rid)
        cu.execute(sql)
        data = cu.fetchone()
        return render_template('edit_product.html',details=data)
    except Exception:
        return "Connection failed !!"
    
@inv_app.route('/update', methods=['POST','GET'])
def update():
    
    pn = request.form['name']
    pr = request.form['price']
    qty = request.form['quantity']
    dt = request.form['date']
    rid = request.form['id']

    try:
        db = pymysql.connect(host="localhost",user="root",password="",db="inv_management")
        cu = db.cursor()
        sql = "update product_details SET name='{}',price='{}',quantity='{}',date='{}' where id='{}'".format(pn,pr,qty,dt,rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
    except Exception:
        return "Connection failed !!"
    
inv_app.run(debug=True)