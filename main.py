from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,  ScreenManager, FadeTransition
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
import random
from kivy.clock import Clock
from kivy.core.window import Window

Builder.load_string("""

<Mainscreen>:
	name: "main"		
	
	MDBottomNavigation:
		
		MDBottomNavigationItem:
			name: "chat"
			text: "Chats"
			icon: "chat-outline"
			
			MDTopAppBar:
				title: "WhatsApp"
				anchor_title: "left"
				right_action_items: [["qrcode-scan"], ["camera-outline"], ["dots-vertical", lambda x: app.callback(x)]]
				md_bg_color: 0,0,0,.5
				title_color: (1,1,1,1)
				pos_hint: {"top":1}
			
			MDBoxLayout:
				orientation: "vertical"
				size_hint_y: None
				height : "900sp"
				pos_hint: {"center_y": .18}
				
				ScrollView:
					size_hint_y: 1
					bar_width: 0
					MDBoxLayout:
						orientation: "vertical"
						size_hint_y: None
						height: self.minimum_height
						
						MDTextField:
							icon_left: "magnify"
							mode: "round"
							hint_text: "Ask Meta AI or Search"
							size_hint_x: .95
							pos_hint: {"center_x": .5}
							font_size: "25sp"
							fill_color_normal: 0,0,0,.5
						
						MDList:
							TwoLineAvatarIconListItem:
								id: item1
								on_release: app.open_chat_screen(self.text)
								text: "Meta AI"
								secondary_text: "Here are the rgba values of black color"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0008.jpg"
									on_release: app.show_profile(self.source , item1.text)
							
							TwoLineAvatarIconListItem:
								id: item11
								on_release: app.open_chat_screen(self.text)
								text: "Chat-GPT"
								secondary_text: "How can i help you today ?"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0011.jpg"
									on_release: app.show_profile(self.source , item11.text)
							
							TwoLineAvatarIconListItem:
								id: item2
								on_release: app.open_chat_screen(self.text)
								text: "AI Assistant"
								secondary_text: "How can I help you"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0006.jpg"
									on_release: app.show_profile(self.source , item2.text)
							TwoLineAvatarIconListItem:
								on_release: app.open_chat_screen(self.text)
								text: "S S ACADEMY"
								secondary_text: "~ + 91 74800 18362 joined"
								IconLeftWidget:
									icon: "account-group"
							TwoLineAvatarIconListItem:
								on_release: app.open_chat_screen(self.text)
								text: "Alex"
								secondary_text: "~ Photo"
								IconLeftWidget:
									icon: "account"
							TwoLineAvatarIconListItem:
								id: item3
								on_release: app.open_chat_screen(self.text)
								text: "Mark Rober"
								secondary_text: "● Missed Voice Call"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0009.jpg"
									on_release: app.show_profile(self.source , item3.text)
							TwoLineAvatarIconListItem:
								id: item4
								on_release: app.open_chat_screen(self.text)
								text: "Mr Beast"
								secondary_text: "Win 1,000,000 dollars"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0007.jpg"
									on_release: app.show_profile(self.source , item4.text)
							TwoLineAvatarIconListItem:
								on_release: app.open_chat_screen(self.text)
								text: "Group"
								secondary_text: "~ +91 246273 has left the group"
								IconLeftWidget:
									icon: "account-group-outline"
							TwoLineAvatarIconListItem:
								on_release: app.open_chat_screen(self.text)
								text: "Samantha"
								secondary_text: "Missed video call"
								IconLeftWidget:
									icon: "face-woman"
									
			MDFloatingActionButton:
				icon: "message-plus"
				pos_hint: {"center_x": .9, "top": .1}
				theme_icon_color: "Custom"
				icon_color: "black"
				icon_size: "25sp"
				md_bg_color: app.theme_cls.primary_color
			
			MDFloatingActionButton:
				icon: "assets/IMG-20250812-WA0008.jpg"
				pos_hint: {"center_x": .9, "top": .18}
				icon_size: "30sp"
				md_bg_color: "#333333"
				type: "small"
				on_release: app.meta_button()
		
		MDBottomNavigationItem:
			name: "update"
			text: "Updates"
			icon: "update"
			
			MDTopAppBar:
				title: "Updates"
				anchor_title: "left"
				right_action_items: [["qrcode-scan"], ["magnify"], ["dots-vertical"]]
				md_bg_color: 0,0,0,.5
				title_color: (1,1,1,1)
				pos_hint: {"top":1}
			
			MDBoxLayout:
				orientation: "vertical"
				pos_hint: {"top": .9}
				
				ScrollView:
					bar_width: 0
					
					MDBoxLayout:
						orientation: "vertical"
						size_hint_y: None
						height: self.minimum_height
						
						MDLabel:
							text: "Status"
							font_size: "20sp"
							bold: True
							pos_hint: {"center_x": .55}
							size_hint_y: None
							height: 70
						
						ScrollView:
							bar_width: 0
							size_hint: None, None
							height: "180sp"
							width: self.parent.width
							do_scroll_y: False
							do_scroll_x: True
							MDBoxLayout:
								orientation: "horizontal"
								size_hint_x: None
								width: self.minimum_width
								spacing: 10
								padding: 30, 0,0,0
								
								MDCard:
									size_hint: None,  None
									size: "100dp", "180dp"
									padding: 10
									md_bg_color: "#333333"
									radius: 30
									FloatLayout:
										MDIconButton:
											icon: "plus"
											pos_hint: {"center_y": .85, "center_x": .3}
											icon_size: "25sp"
											theme_icon_color: "Custom"
											icon_color: 0,0,0,1
											md_bg_color: app.theme_cls.primary_color
										MDLabel:
											text: "Add status"
											bold: True
											pos_hint: { "center_x": .55, "center_y": .1}
								MDCard:
									size_hint: None,  None
									size: "100dp", "180dp"
									padding: 10
									md_bg_color: "#333333"
									radius: 30
									FloatLayout:
										FitImage:
											source: "assets/IMG-20250812-WA0010.jpg"
											pos_hint: {"center_x": .5, "top":1}
										MDIconButton:
											icon: "assets/IMG-20250812-WA0009.jpg"
											pos_hint: {"center_y": .85, "center_x": .3}
											icon_size: "30sp"
										MDLabel:
											text: "Mark Rober"
											bold: True
											pos_hint: { "center_x": .55, "center_y": .1}
								MDCard:
									size_hint: None,  None
									size: "100dp", "180dp"
									padding: 10
									md_bg_color: "#333333"
									radius: 30
									FloatLayout:
										FitImage:
											source: "assets/IMG-20250812-WA0004.jpg"
											pos_hint: {"center_x": .5, "top": 1}
										MDIconButton:
											icon: "assets/IMG-20250812-WA0007.jpg"
											pos_hint: {"center_y": .85, "center_x": .3}
											icon_size: "30sp"
										MDLabel:
											text: "Mr Beast"
											bold: True
											pos_hint: { "center_x": .55, "center_y": .1}
								MDCard:
									size_hint: None,  None
									size: "100dp", "180dp"
									padding: 10
									md_bg_color: 0,1,0,.1
									radius: 30
									FloatLayout:
										MDIconButton:
											icon: "account"
											pos_hint: {"center_y": .85, "center_x": .3}
											icon_size: "25sp"
										MDLabel:
											text: "Alex"
											bold: True
											pos_hint: { "center_x": .55, "center_y": .1}
								MDCard:
									size_hint: None,  None
									size: "100dp", "180dp"
									padding: 10
									md_bg_color: 1,1,1,.5
									radius: 30
									FloatLayout:
										MDIconButton:
											icon: "face-woman"
											pos_hint: {"center_y": .85, "center_x": .3}
											icon_size: "25sp"
										MDLabel:
											text: "Samantha"
											bold: True
											pos_hint: { "center_x": .55, "center_y": .1}
						
						MDBoxLayout:
							orientation: "horizontal"
							size_hint: (1 , None)
							height: self.minimum_height + 10
							pos_hint: {"center_x": .53}
							padding: 10
							
							MDLabel:
								text: "Channels"
								pos_hint: {"center_x": .55}
								font_size: "20sp"
								bold: True
							MDRectangleFlatButton:
								text: "Explore  >"
								theme_text_color: "Custom"
								text_color: app.theme_cls.primary_color
								line_color: 0,0,0,0
								font_size: "15sp"
								pos_hint:{ "center_y": .5}
						
						MDList:
							TwoLineAvatarIconListItem:
								id: channel1
								text: "BTS | RM,Namjoon Jin,Kim Taehyung"
								secondary_text: "BTS Playlist is live on Spotify, and we need"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0014.jpg"
									on_release: app.show_profile(self.source , channel1.text)
							
							TwoLineAvatarIconListItem:
								id: channel2
								text: "Kim Taehyung"
								secondary_text: "Photo ■ "
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0016.jpg"
									on_release: app.show_profile(self.source , channel2.text)
							
							TwoLineAvatarIconListItem:
								id: channel3
								text: "Jin"
								secondary_text: "BTS Playlist is live on Spotify, and we need"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0013.jpg"
									on_release: app.show_profile(self.source , channel3.text)
							
							TwoLineAvatarIconListItem:
								id: channel4
								text: "jhope"
								secondary_text: "BTS Playlist is live on Spotify, and we need"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0012.jpg"
									on_release: app.show_profile(self.source , channel4.text)
							
							TwoLineAvatarIconListItem:
								id: channel5
								text: "SUGA"
								secondary_text: "BTS Playlist is live on Spotify, and we need"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0005.jpg"
									on_release: app.show_profile(self.source , channel5.text)
			
			MDFloatingActionButton:
				icon: "camera-plus"
				md_bg_color: app.theme_cls.primary_color
				pos_hint: {"center_x": .9 , "top": .1}
				theme_icon_color: "Custom"
				icon_color: "black"
				icon_size: "25sp"
			MDFloatingActionButton:
				icon: "pencil"
				md_bg_color: "#333333"
				pos_hint: {"center_x": .9 , "top": .18}
				icon_size: "30sp"
				type: "small"
		
		MDBottomNavigationItem:
			name: "community"
			text: "Communities"
			icon: "account-group-outline"
			
			MDTopAppBar:
				title: "Communities"
				anchor_title: "left"
				right_action_items: [["qrcode-scan"], ["dots-vertical"]]
				md_bg_color: 0,0,0,.5
				title_color: (1,1,1,1)
				pos_hint: {"top":1}
				
			MDFloatLayout:
				md_bg_color: "black"
				pos_hint: {"top": .92}
				
				FitImage:
					source: "assets/IMG-20250812-WA0017.jpg"
					pos_hint: {"center_x": .5, "top": .9}
					size_hint: 1, .3
					allow_stretch: True
					keep_ratio: False
				
				MDLabel:
					text: "Stay connected with a\\ncommunity"
					bold: True
					halign: "center"
					pos_hint: {"center_x": .52, "center_y": .55}
					font_size: "20sp"
				
				MDLabel:
					text: "Communities bring members together in topic-\\nbased groups, and make it easy to get admin\\nannouncements. Any community you're added to\\nwill appear here."
					halign: "center"
					pos_hint: {"center_x": .51, "center_y": .45}
					theme_text_color: "Secondary"
				
				MDFlatButton:
					text: "See example\\ncommunities"
					pos_hint: {"center_x": .51 , "center_y": .35}
					theme_text_color: "Custom"
					text_color: app.theme_cls.primary_color
				
				MDFillRoundFlatButton:
					text: "Start your community"
					md_bg_color: app.theme_cls.primary_color
					font_size: "15sp"
					size_hint_x: .8
					pos_hint: {"center_x": .5, "center_y": .25}


		MDBottomNavigationItem:
			name: "call"
			text: "Calls"
			icon: "phone"
			
			MDTopAppBar:
				title: "Calls"
				anchor_title: "left"
				right_action_items: [["qrcode-scan"], ["magnify"], ["dots-vertical"]]
				md_bg_color: 0,0,0,.5
				title_color: (1,1,1,1)
				pos_hint: {"top":1}
			
			MDBoxLayout:
				orientation: "vertical"
				pos_hint: {"top": .9}
				#md_bg_color: "red"
				
				MDScrollView:
					bar_width: 0
					
					MDBoxLayout:
						orientation: "vertical"
						size_hint_y: None
						height: self.minimum_height
						
						MDLabel:
							text: "Favourites"
							bold: True
							pos_hint: {"center_x": .55}
							size_hint_y: None
							height: 100
						MDList:
							OneLineIconListItem:
								text: "Add favourite"
								IconLeftWidget:
									icon: "heart"
						MDLabel:
							text: "Recent"
							bold: True
							pos_hint: {"center_x": .55}
							size_hint_y: None
							height: 50
						MDList:
							TwoLineAvatarIconListItem:
								text: "Mr Beast"
								secondary_text: "15 March, 3:44 pm"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0007.jpg"
								IconRightWidget:
									icon: "phone"
							TwoLineAvatarIconListItem:
								text: "Mark Rober"
								secondary_text: "17 March, 1:30 pm"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0009.jpg"
								IconRightWidget:
									icon: "phone"
							TwoLineAvatarIconListItem:
								text: "Kim Taehyung"
								secondary_text: "22 March, 4:00 pm"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0016.jpg"
								IconRightWidget:
									icon: "phone"
							TwoLineAvatarIconListItem:
								text: "Jin"
								secondary_text: "21 March, 3:55 pm"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0013.jpg"
								IconRightWidget:
									icon: "phone"
							TwoLineAvatarIconListItem:
								text: "Samantha"
								secondary_text: "19 March, 1:13 pm"
								IconLeftWidget:
									icon: "face-woman"
								IconRightWidget:
									icon: "phone"
							TwoLineAvatarIconListItem:
								text: "jhope"
								secondary_text: "25 March, 11:24 am"
								ImageLeftWidget:
									source: "assets/IMG-20250812-WA0012.jpg"
								IconRightWidget:
									icon: "phone"
			
			MDFloatingActionButton:
				icon: "phone-plus"
				md_bg_color: app.theme_cls.primary_color
				pos_hint: {"center_x": .9 , "top": .1}
				theme_icon_color: "Custom"
				icon_color: "black"
				icon_size: "25sp"
				

<ChatScreen>:
	name: "chatscreen"
	
	MDTopAppBar:
		id: topbar
		title: ""
		pos_hint: {"top": 1}
		left_action_items: [["arrow-left", lambda x: root.go_back()]]
		right_action_items: [["video-outline"], ["phone"], ["dots-vertical"]]
		md_bg_color: "black"
		title_color: 1,1,1,1
		anchor_title: "left"
	
	MDBoxLayout:
		id: scroll_area
		orientation: "vertical"
		pos_hint: {"top": .91}
		size_hint_y: .84
		padding: 10
		#md_bg_color: "red"
		
		MDScrollView:
			#md_bg_color: "blue"
		
			MDBoxLayout:
				id: chat
				orientation: "vertical"
				padding: 30
				spacing: 20
				size_hint_y: None
				#pos_hint: {"top": .92}
				height: self.minimum_height
				#md_bg_color: "red"
		
	
	MDTextField:
		id: msg
		multiline: True
		hint_text: "Message"
		mode: "rectangle"
		fill_color_normal: "#333333"
		size_hint_x: .8
		font_size: "15sp"
		pos_hint: {"center_y": .05, "center_x": .43}
		icon_left: "sticker-emoji"
		on_focus: app.adjust_view(self , self.focus)
	
	MDIconButton:
		id: send_button
		icon: "microphone"
		md_bg_color: app.theme_cls.primary_color
		pos_hint:{ "center_x": .9, "center_y": .04}
		theme_icon_color: "Custom"
		icon_color: "black"
		on_release: app.send_message()
	MDIconButton:
		id: paperclip
		icon: "paperclip"
		pos_hint: {"center_x": .75, "center_y": .04}
		icon_size: "23sp"

<Profile>:
	orientation: "vertical"
	size_hint_y: None
	height: "250dp"
	
	FitImage:
		id: picture
		source: ""
		size_hint_y: None
		height: "200sp"
	
	BoxLayout:
		orientation: "horizontal"
		size_hint_y: None
		height: "50sp"
		spacing: 30
		size_hint_x: 1
		padding: 30,0,0,0
		
		MDIconButton:
			icon: "message-processing-outline"
			theme_icon_color: "Custom"
			icon_color: app.theme_cls.primary_color
		MDIconButton:
			icon: "phone"
			theme_icon_color: "Custom"
			icon_color: app.theme_cls.primary_color
		MDIconButton:
			icon: "video-outline"
			theme_icon_color: "Custom"
			icon_color: app.theme_cls.primary_color
		MDIconButton:
			icon: "information-outline"
			theme_icon_color: "Custom"
			icon_color: app.theme_cls.primary_color

<Setting>:
	
	MDTopAppBar:
		title: "Settings"
		left_action_items: [["arrow-left", lambda x: root.go_back()]]
		right_action_items: [["magnify"]]
		pos_hint: {"top": 1}
		md_bg_color: "black"
		title_color: 1,1,1,1
		anchor_title: "left"
		
	MDBoxLayout:
		orientation: "vertical"
		pos_hint: {"top": .92}
		#md_bg_color: "red"
		
		MDScrollView:
			
			BoxLayout:
				orientation: "vertical"
				size_hint_y: None
				height: self.minimum_height
				
				ThreeLineAvatarIconListItem:
					text: "Navjot Singh"
					secondary_text: "I made this whatsapp clone"
					tertiary_text: "  "
					size_hint_y: None
					height: "100dp"
					IconLeftWidget:
						icon: "account-arrow-right"
						icon_size: "40sp"
					IconRightWidget:
						icon: "qrcode"
						theme_icon_color: "Custom"
						icon_color: app.theme_cls.primary_color
						
				TwoLineAvatarIconListItem:
					text: "Account"
					secondary_text: "Security notificatios, change number"
					IconLeftWidget:
						icon: "key-outline"
				TwoLineAvatarIconListItem:
					text: "Privacy"
					secondary_text: "Block contacts, dissappearing messages"
					IconLeftWidget:
						icon: "lock-outline"
				TwoLineAvatarIconListItem:
					text: "Avatar"
					secondary_text: "Create, edit, profile photo"
					IconLeftWidget:
						icon: "face-man-profile"
				TwoLineAvatarIconListItem:
					text: "Lists"
					secondary_text: "Manage people and groups"
					IconLeftWidget:
						icon: "account-box-multiple-outline"
				TwoLineAvatarIconListItem:
					text: "Chats"
					secondary_text: "Theme, wallpapers,  chat history"
					IconLeftWidget:
						icon: "message-bulleted"
				TwoLineAvatarIconListItem:
					text: "Notifications"
					secondary_text: "Message, group and call tones"
					IconLeftWidget:
						icon: "bell-outline"
				TwoLineAvatarIconListItem:
					text: "Storage and data"
					secondary_text: "Network usage, auto download"
					IconLeftWidget:
						icon: "database"
				TwoLineAvatarIconListItem:
					text: "App language"
					secondary_text: "English (device's language"
					IconLeftWidget:
						icon: "web"
				TwoLineAvatarIconListItem:
					text: "Help"
					secondary_text: "Help center, contact us, privacy policy"
					IconLeftWidget:
						icon: "help-circle-outline"
				OneLineIconListItem:
					text: "Invite a friend"
					IconLeftWidget:
						icon: "account-multiple-outline"
				
				MDLabel:
					text: "Also from Meta"
					pos_hint:{ "center_x": .55}
					size_hint_y: None
					height: "70sp"
					color: "#939492"
				
				OneLineIconListItem:
					text: "Open Instagram"
					IconLeftWidget:
						icon: "instagram"
				OneLineIconListItem:
					text: "Open Facebook"
					IconLeftWidget:
						icon: "facebook"
				OneLineIconListItem:
					text: "Open Threads"
					IconLeftWidget:
						icon: "gesture"
				
""")

class Mainscreen(Screen):
	pass

class Chatscreen(Screen):
	
	def go_back(self):
		self.manager.current = "main"

class Profile(BoxLayout):
	pass

class Setting(Screen):
	
	def go_back(self):
		self.manager.current = "main"

class WhatsApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Teal"
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.accent = "Teal"
		Window.size = (400,718)
		sm=ScreenManager(transition=FadeTransition(duration=0.2))
		sm.add_widget(Mainscreen(name="main"))
		sm.add_widget(Chatscreen(name="chatscreen"))
		sm.add_widget(Setting(name="setting"))
		#sm.current = "chatscreen"
		menu_items = [{"viewclass": "OneLineListItem", 
										"text": "New group", "height":dp(56)}, {"viewclass":"OneLineListItem",  "text":"New broadcast", "height":dp(56)}, {"viewclass":"OneLineListItem", "text":"Linked devices","height":dp(56)}, {"viewclass":"OneLineListItem",  "text":"Starred messages", "height":dp(56)}, {"viewclass":"OneLineListItem", "text":"Payments", "height":dp(56)}, {"viewclass": "OneLineListItem","text": "Settings", "height":dp(56), "on_release": lambda: self.go_to_setting()}]
		self.menu = MDDropdownMenu(width_mult = 1, items=menu_items)
		
		return sm

	def open_chat_screen(self, chat_name):
		chat_screen = self.root.get_screen("chatscreen")
		chat_screen.ids.topbar.title = chat_name
		self.root.current = "chatscreen"
	
	def adjust_view(self ,widget, focus):
		chat_screen = self.root.get_screen("chatscreen")
		if focus:
			chat_screen.ids.send_button.icon = "send"
		
		else:
			chat_screen.ids.send_button.icon = "microphone"
			
	def send_message(self):
		chat_screen = self.root.get_screen("chatscreen")
		
		if chat_screen.ids.msg.text != "":
			self.execute_message(chat_screen.ids.msg.text, "#075E54", 0.75, [40,0,40,40])
			self.event = Clock.schedule_interval(self.receive_message , 2)
			
		else:
			pass
	
	def receive_message(self, dt):
		fake_messages = ["Hey, how's it going?",
		"What are you up to?",
		"Sorry, just saw your message",
		"Can't talk right now, I'll call you later",
		"Sounds good to me!",
		"I'm not sure about that",
		"Let me think about it",
		"When are you free to meet?",
		"Where should we go?",
		"I'll be there in 10 minutes",
		"Running a bit late, sorry!",
		"Did you see the game last night?",
		"What do you think about this?",
		"That's funny!",
		"LOL",
		"Haha",
		"Okay",
		"Sure thing",
		"No problem",
		"Thanks for letting me know",
		"Can you send me that file?",
		"I'll check and get back to you",
		"How was your day?",
		"Any plans for the weekend?",
		"Call me when you get a chance",
		"I'm at the store, need anything?",
		"See you soon!",
		"On my way",
		"Got it, thanks",
		"You're right about that",
		"I agree",
		"Not sure I understand",
		"Can you explain that again?",
		"Let's catch up soon",
		"Miss you!",
		"How's the family?",
		"What time should we meet?",
		"I'm tired today",
		"That's awesome!",
		"I'm happy for you",
		"That's too bad",
		"I'm sorry to hear that",
		"Hope you feel better soon",
		"Good morning!",
		"Good night!",
		"Talk to you tomorrow",
		"Let me know how it goes",
		"Thinking of you",
		"Can I call you later?",
		"What's new with you?"]
		
		fake_response = random.choice(fake_messages)
		
		self.execute_message(fake_response, '#171f19', 0.25, [0,40,40,40])
		Clock.unschedule(self.event)
	
	def execute_message(self, text, color, pos, radius):
		chat_screen = self.root.get_screen("chatscreen")
		card = MDCard(
				padding="10dp",
				radius=radius,
				size_hint=(None, None),
				md_bg_color=color,
				elevation=3,
				pos_hint={"center_x":pos}
			)
		label = MDLabel(
			text=text,
			size_hint=(None,None),
			width="150dp",
			halign = "left",
			pos_hint={"center_y":.5}
			)
		label.bind(texture_size=label.setter("size"))
			
		card.add_widget(label)

		card.width = label.width + 30
		card.height = label.height+ 10

		chat_screen.ids.chat.add_widget(card)

		chat_screen.ids.msg.text = ""
	
	def meta_button(self):
		chat_screen = self.root.get_screen("chatscreen")
		self.root.current = "chatscreen"
		chat_screen.ids.topbar.title = "Meta AI"
	
	def show_profile(self, img, name):
		content = Profile()
		content.ids.picture.source = img
		self.dialog = MDDialog(
					title= name,
					type="custom",
					content_cls= content,)
		self.dialog.open()
	
	def callback(self, button):
		self.menu.caller = button
		self.menu.open()
	
	def go_to_setting(self):
		self.root.current = "setting"
		self.menu.dismiss()

WhatsApp().run()