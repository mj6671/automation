# 80% win rate 
import pyautogui as pgs
import time
pgs.PAUSE=0.4
pgs.FAILSAFE=True
time.sleep(4)
'''class find_theimg:
 def __init__(self,img:str,a):
          self.img=img
          self.a=a'''
def the_img_on_screen(img:str,a):
          if a!=0:
                    pgs.hscroll(-400)
                    pgs.sleep(2)
                    next=pgs.locateAllOnScreen(img,confidence=0.80)
                    for x in (next):
                      print(x)
                      pgs.click(x)
                      pgs.write('good')
                      a-=1
                     #return a
          else:
                    pgs.click('enter')         
          
          
                                        
if __name__=='__main__':
          a=25
          img_a='feedback_4.png'
          pos=pgs.locateAllOnScreen(img_a,confidence=0.80)
          for x in (pos):
            print(x)
            pgs.click(x)
            pgs.write('good')
            a-=1
          the_img_on_screen(img_a,a)
          #the_img_on_screen(img_a,a)
          '''if a==0:
                    pgs.click('enter')
          elif a!=0:
                    pgs.hscroll(-100)
                    the_img_on_screen(img_a,a)
                    
          else:
                    pgs.click("update")'''


          
           
          
