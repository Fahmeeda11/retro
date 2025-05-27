from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3



#initialize flask
app = Flask(__name__)
CORS(app)

#index
@app.route('/')
def index():
    return 'Retro Board API is running. Use /boards to interact.', 200

#post board 
@app.route('/boards', methods=['POST'])
def single_boards():
    try:
        data = request.get_json()
        board_name = data.get('board_name') # this one takes the parameter/key name board_name and takes value from it from the payload
        description = data.get('description', '') # same as above
        if not board_name:
            return jsonify({'error': 'Board name is required'}), 400
        conn = sqlite3.connect('retroboard.db') # this line connects the db
        cursor = conn.cursor()

        cursor.execute( # this one is executing the query with the values we got
            'INSERT INTO boards (board_name, description) VALUES (?, ?)',
            (board_name, description)
        )
        board_id = cursor.lastrowid
        print("DEBUG: Inserted board_id =", board_id)  # Add this line

        conn.commit()
        conn.close()

        return jsonify({
            'message': 'Board created successfully',
            'board_id': board_id
        }), 201 # we're returning this response back

    except Exception as e:
        return jsonify({'error': str(e)}), 500

#get boards
@app.route('/get_boards',methods=['GET'])
def get_boards():
    try:
        conn = sqlite3.connect('retroboard.db')
        cursor = conn.cursor()

        #select data
        cursor.execute('SELECT * FROM boards')
        rows = cursor.fetchall()
        conn.close()

        #create list for boards
        boards = [{
            'board_id': row[0],
            'board_name': row[1],
            'description': row[2]
        } for row in rows]
        
        return jsonify(boards)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


#added
@app.route('/boards/<int:board_id>', methods=['GET'])
def get_board(board_id):
    try:
        conn = sqlite3.connect('retroboard.db'
        )
        cursor = conn.cursor()
        
        cursor.execute('SELECT board_id, board_name, description FROM boards WHERE board_id = ?', (board_id,))
        board = cursor.fetchone()
        conn.close()
        
        if not board:
            return jsonify({'error': 'Board not found'}), 404
            
        return jsonify({
            'board_id': board[0],
            'board_name': board[1],
            'description': board[2]
        }), 200
        
    except Exception as e:
        print(f"ERROR in get_board: {str(e)}")
        return jsonify({'error': str(e)}), 500

    
if __name__ == '__main__':
    app.run(debug=True)    
    
