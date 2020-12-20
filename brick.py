import pygame as pg,random, math
pg.init()

class Ball(pg.sprite.Sprite):
	dx = 0         #x位移量
	dy = 0         #y位移量
	x = 0          #球x坐標
	y = 0          #球y坐標
	direction = 0  #球移動方向
	speed = 0      #球移動速度

	def __init__(self, sp, srx, sry, radium, color):
		pg.sprite.Sprite.__init__(self)
		self.speed = sp
		self.x = srx
		self.y = sry
		self.radium = radium
		#繪製球體
		self.image = pg.Surface([radium*2, radium*2])  
		self.image.fill((255,255,255))
		pg.draw.circle(self.image, color, (radium,radium), radium, 0)
		self.rect = self.image.get_rect()  #取得球體區域
		self.rect.center = (srx,sry)       #初始位置
		self.direction = random.randint(40,70)  #移動角度

         #球體移動 
	def update(self):         
		radian = math.radians(self.direction)    #角度轉為弳度
		self.dx = self.speed * math.cos(radian)  #球水平運動速度
		self.dy = -self.speed * math.sin(radian) #球垂直運動速度
		self.x += self.dx     #計算球新坐標
		self.y += self.dy
		self.rect.x = self.x  #移動球圖形
		self.rect.y = self.y
        #到達左右邊界
		if(self.rect.left <= 0 or self.rect.right >= screen.get_width()-10):  
			self.bouncelr()
		elif(self.rect.top <= 10):  #到達上邊界
			self.rect.top = 10
			self.bounceup()
		if(self.rect.bottom >= screen.get_height()-10):  #到達下邊界出界
			return True
		else:
			return False
	def large(self):
		self.image = pg.Surface([40, 40])  
		self.image.fill((207,78,168))
		pg.draw.circle(self.image, (207,78,168), (20,20), 20, 0)
		#self.rect = self.image.get_rect()  #取得球體區域
		#self.rect.center = (20,20)       #初始位置
		#self.direction = random.randint(40,70)  #移動角度


	def bounceup(self):
		self.direction = 360 - self.direction
	
	def bouncelr(self):
		self.direction = (180 - self.direction) % 360

class Brick(pg.sprite.Sprite):
	def __init__(self, color, x, y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface([38,13])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y




score = 0  #得分
dfont = pg.font.SysFont("Arial", 20)    #下方訊息字體
ffont = pg.font.SysFont("SimHei", 32)   #結束程式訊息字體

#背景
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("Brick Game")
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
allsprite = pg.sprite.Group()  #建立全部角色群組
bricks = pg.sprite.Group()     #建立磚塊角色群組
ball = Ball(15, 300, 350, 10, (255,123,188)) #建立粉球
allsprite.add(ball)  #加入全部角色群組
#pad = Pad()          #建立滑板球物件
#allsprite.add(pad)   #加入全部角色群組

for row in range(5):
	for column in range(15):
		if row == 0:
			brick = Brick((255,0,0), column*40 + 1, row*15 + 1, )
		if row == 1:
			brick = Brick((255,201,14), column*40 + 1, row*15 + 1, )
		if row == 2:
			brick = Brick((255,255,0), column*40 + 1, row*15 + 1, )
		if row == 3:
			brick = Brick((0,255,0), column*40 + 1, row*15 + 1, )
		if row == 4:
			brick = Brick((0,0,255), column*40 + 1, row*15 + 1, )
		bricks.add(brick)
		allsprite.add(brick)

class tab(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface([700,25])
		self.image.fill((230,230,230))
		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = 360


#		(a,b) = pg.mouse.get_pos()
#		self.tab = pg.draw.rect(background,(230,230,230),[a+50,360,100,25],0)


	def update(self):
		(a,b) = pg.mouse.get_pos()
		self.rect.x = a
		#self.rect.y = b

class cross(pg.sprite.Sprite):
	x = 0          #球x坐標
	y = 0          
	speed = 0      #球移動速度

		#繪製球體
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load("..\\cross.jfif")
		self.image.convert()
		self.image = pg.transform.scale(self.image,(50,50))
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0,600)
		self.rect.y = -30


         #球體移動 
	def update(self):         
		self.speed = 7
		self.rect.y += self.speed

class Lightning(pg.sprite.Sprite):
	x = 0          #球x坐標
	y = 0          
	speed = 0      #球移動速度

		#繪製球體
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load("..\\yellow-lightning-png-31.png")
		self.image = pg.transform.scale(self.image,(50,50))
		self.image.convert()
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0,600)
		self.rect.y = -30
		#self.x = 
		#self.y = -30


         #球體移動 
	def update(self):         
		self.speed = 7
		self.rect.y += self.speed

tab = tab()
allsprite.add(tab)
Lightning = Lightning()
Lightnings = pg.sprite.Group()
Lightnings.add(Lightning)
allsprite.add(Lightning)
cross = cross()
crosss = pg.sprite.Group()
crosss.add(cross)
allsprite.add(crosss)

clock = pg.time.Clock()        
downmsg = "Press Left Click Button to start game!"  #起始訊息
playing = False  #開始時球不會移動
running = True
tab_key = True
#運行的程式碼
while running:
	clock.tick(30)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
	buttons = pg.mouse.get_pressed()  #檢查滑鼠按鈕
	if buttons[0]:            #按滑鼠左鍵後球可移動       
		playing = True
        
    #遊戲進行中
	if playing == True:  
		screen.blit(background, (0,0))  #清除繪圖視窗
		fail = ball.update()  #移動球體
		cross.update()
		Lightning.update()
		if fail:
        
			font = pg.font.SysFont("Arial",50)
			gameover = font.render('GAME OVER', True, (0,0,0), (255,255,255))
			screen.blit(gameover, (175,175))
			tab_key = False

        #if fail:              #球出界
            #gameover("You failed!See you next time~")
		
		if tab_key:
			tab.update()          #更新滑板位置

        #檢查球和磚塊碰撞
		hitbrick = pg.sprite.spritecollide(ball, bricks, True)  
		if len(hitbrick) > 0:  #球和磚塊發生碰撞
			score += len(hitbrick)  #計算分數
			ball.rect.y += 20  #球向下移
			ball.bounceup()    #球反彈
			if len(bricks) <= 40:  #所有磚塊消失
				font = pg.font.SysFont("Arial",50)
				win = font.render('YOU  WIN!!!', True, (212,201,106), (255,255,255))
				ball.rect.y = 0
				ball.speed = 0
				tab_key = False
				screen.blit(win, (175,175))
				playing = False
		hitlight = pg.sprite.spritecollide(tab, Lightnings, True)  
		if len(hitlight) > 0:  #球和磚塊發生碰撞
			tab.image = pg.Surface([200,25])
		hitcross = pg.sprite.spritecollide(tab, crosss, True)  
		if len(hitcross) > 0:  #球和磚塊發生碰撞
			ball.large()
			#ball.image.radium = 20
			#ball.image.fill([207,78,168])
		hitpad = pg.sprite.collide_rect(ball, tab)
		if hitpad:  #球和滑板發生碰撞
			ball.bounceup()  #球反彈
		allsprite.draw(screen)  #繪製所有角色
		downmsg = "Score: " + str(score)
    #繪製下方訊息        
	message = dfont.render(downmsg, 1, (255,0,255))
	screen.blit(message, (screen.get_width()/2-125,screen.get_height()-30))
	pg.display.update()
pg.quit()
