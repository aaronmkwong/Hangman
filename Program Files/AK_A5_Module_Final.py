
class font:
    """format text so as to be pleasing or amusing to the user"""
  
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yello = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'   
    
class hangman_words:
    """import words to guess data, convert to a single list and randomly select a word"""
    
    def __init__(self):
        import pandas as pd
        data = pd.read_csv('data_science_terms.csv')
        data_lists = data.values.tolist()
        words_list = [y for x in data_lists for y in x]
        import random 
        self.word = random.choice(words_list) 
                
def hangman_image(x):
    """import picture data for each incorrect word or letter penalty, convert to a single list and display"""
    
    import matplotlib.pyplot as plt
    import matplotlib.image as read
    
    img0 = read.imread('Hangman_0.png')
    img1 = read.imread('Hangman_1.png')
    img2 = read.imread('Hangman_2.png')
    img3 = read.imread('Hangman_3.png')
    img4 = read.imread('Hangman_4.png')
    img5 = read.imread('Hangman_5.png')
    img6 = read.imread('Hangman_6.png')
    
    img_list = [img0,img1,img2,img3,img4,img5,img6]
    
    return (plt.axis('off'),
            plt.imshow(img_list[x]),
            plt.show())

        
        
        
        

    

    
            