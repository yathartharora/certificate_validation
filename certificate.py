import cv2 as cv
import openpyxl
import datetime
import hashlib
import json
import ipfsApi


api = ipfsApi.Client('127.0.0.1',5001)
#Blockchain implementation


class Blockchain:

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof = 1,previous_hash = '0')
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain)+1 ,
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' : proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions }
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof = new_proof + 1

        return new_proof

    def hash(self,block):
        encoded_block = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()


    def add_transaction(self,filename):
        self.transactions.append(filename)

        previous_block = self.get_previous_block()
        return previous_block['index']+1

    def mine_block(bl):
        previous_block = bl.get_previous_block()
        previous_proof = previous_block['proof']
        proof = bl.proof_of_work(previous_proof)
        previous_hash = bl.hash(previous_block)
        block = bl.create_block(proof, previous_hash)
        response = {'message': "Congratulations, you just mined a block",
                    'index':block['index'],
                    'timestamp': block['timestamp'],
                    'proof': block['proof'],
                    'previous_hash':block['previous_hash']
                    }
        return response['message']


    def get_chain(bl):
        response = {'chain': bl.chain,
                'length': len(bl.chain)
                }
        return response

    def get_previous_hash(bl):
        previous_block = bl.get_previous_block()
        previous_proof = previous_block['previous_hash']
        return previous_proof
        
    def get_previous_index(bl):
        previous_block = bl.get_previous_block()
        previous_index = previous_block['index']
        return previous_index



block = Blockchain()
block.mine_block()


template_path = '/Users/yathartharora/certificate_validation/template_certificate.png'
details_path = '/Users/yathartharora/certificate_validation/details.xlsx'
output_path = '/Users/yathartharora/certificate_validation/'



font_size = 3
font_color = (0,0,0)


coordinate_y_adjustment = -30
coordinate_x_adjustment = 10


obj = openpyxl.load_workbook(details_path)
sheet = obj.active


for i in range(3,5):
    
    proof = block.get_previous_hash()
    print(proof)
    get_name = sheet.cell(row = i ,column = 1)
    certi_name = get_name.value
    block.add_transaction(proof)
    
    
    img = cv.imread(template_path)

    font = cv.FONT_HERSHEY_PLAIN

    text_size = cv.getTextSize(certi_name, font, font_size, 10)[0]
    text_x = (img.shape[1] - text_size[0]) / 2 + coordinate_x_adjustment
    text_y = (img.shape[0] + text_size[1]) / 2 - coordinate_y_adjustment
    text_x = int(text_x)
    text_y = int(text_y)

    cv.putText(img, certi_name, (text_x ,text_y ), font, font_size, font_color, 2)
    cv.putText(img, proof, (190 ,680), font, 1, font_color, 2)

    certi_path = output_path + certi_name + '.png'

    cv.imwrite(certi_path,img)
    res = api.add(certi_name + '.png')
    block.add_transaction(res)
    block.mine_block()
    
    
print(block.get_chain())
cv.destroyAllWindows()



