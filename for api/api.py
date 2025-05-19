from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import sys
import inspect
import os
#initialize flask
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return 'Retro Board API is running. Use /boards to interact.', 200
#giving db path
retrodb = 'retroboard.db'
#added niw


#function to connect databas
def retro_db_connect():
    db_connect = sqlite3.connect(retrodb)
    db_connect.row_factory = sqlite3.Row
    return db_connect
#get board 
@app.route('/boards', methods=['POST'])
def single_boards():
    try:
        data = request.get_json()
        board_name = data['board_name']
        description = data.get('description', '')
        if not board_name:
            return jsonify({'error': 'Board name is required'}), 400
        createb = retro_db_connect()
        cursor = createb.cursor()

        cursor.execute(
            'INSERT INTO boards (board_name, description) VALUES (?, ?)',
            (board_name, description)
        )
        board_id = cursor.lastrowid
        createb.commit()
        createb.close()
    except Exception as e:
        return jsonify({'error': str(e)}), 500


#create board
@app.route('/boards', methods=['GET'])
def get_boards():
    try:
        conn = retro_db_connect()
        boards = conn.execute('SELECT * FROM boards').fetchall()
        conn.close()
        
        boards_list = [dict(board) for board in boards]
        return jsonify({'boards': boards_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)    
    
