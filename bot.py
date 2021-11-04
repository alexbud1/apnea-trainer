import telebot
from telebot import types
from diagrams_training import draw_apnea 
from diagrams_training import draw_cwf
from checker import check_value_return_data
from checker import check_cwf
from diagrams_training import delete_graphic
from diagrams_training import clear_file
from diagrams_training import delete_last_string
from diagrams_training import check_progress
from diagrams_training import delete_cwf
from diagrams_training import clear_cwf
from diagrams_training import delete_last_string_cwf
from diagrams_training import check_progress_cwf

###Token inizialization
#####3
client = telebot.TeleBot('1896014937:AAHNjNpC_xWpChqnLqcE8dtZlzIp_welePs')

###Main menu keyboard
main_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
main_keyboard.row('⬆️Train your skills', '📗 Some info')
####Disciplines keyboard
keyboard_train = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
keyboard_train.row('⚠️ CWF','↔️ Dynamic')
keyboard_train.row('◀️ Back','⏱ Apnea')




###Behaviour on start command
@client.message_handler(commands = ['start'])
def get_bot_started(message):
	client.send_message(message.chat.id, '''*Hi,there! If you are going to work with bot - make a look which opportunities are avaible in keyboard.*''',reply_markup = main_keyboard, parse_mode="Markdown")




###Behaviour on text
@client.message_handler(content_types = ['text'])

###Main menu function
def get_text_main(message):
	if message.from_user.id == 645595220:
		if message.text == '⬆️Train your skills':
			someStep = client.send_message(message.chat.id, 'Let\'s create some infographics',reply_markup= keyboard_train)
			client.register_next_step_handler(someStep, get_text_Train)
		if message.text == '📗 Some info':
			# someStep = 
			client.send_message(message.chat.id, 'Here you can find out important information about freediving and read a piece of advice.')
			# client.register_next_step_handler(someStep, get_text_Info)

####Disciplines function
def get_text_Train(message):
	keyboard_train = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_train.row('⚠️ CWF','↔️ Dynamic')
	keyboard_train.row('◀️ Back','⏱ Apnea')

	keyboard_cwf = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_cwf.row('◀️ Back','⬆️Train')
	keyboard_cwf.row('🗑 Clear data','🖍 Delete last attempt')
	keyboard_cwf.row('📊 View progress')


	keyboard_dynamic = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_dynamic.row('◀️ Back','⬆️Train')

	keyboard_apnoe = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_apnoe.row('◀️ Back','⬆️Train')
	keyboard_apnoe.row('🗑 Clear data','🖍 Delete last attempt')
	keyboard_apnoe.row('📊 View progress')


	if message.text == '⚠️ CWF':
		someStep = client.send_message(message.chat.id, 'In this section you can control your Constant Weight Freediving progress',reply_markup= keyboard_cwf)
		client.register_next_step_handler(someStep, cwf_training)
	if message.text == '↔️ Dynamic':
		someStep = client.send_message(message.chat.id, 'In this section you can control your Dynamic Freediving progress',reply_markup= keyboard_dynamic)
		client.register_next_step_handler(someStep, dynamic_training)
	if message.text == '⏱ Apnea':
		someStep = client.send_message(message.chat.id, 'In this section you can control your Static Breathhold progress',reply_markup= keyboard_apnoe)
		client.register_next_step_handler(someStep, apnea_training)
	if message.text == '◀️ Back':
		someStep = client.send_message(message.chat.id, 'Returning to main menu...', reply_markup = main_keyboard)
		client.register_next_step_handler(someStep, get_text_main)


######start deep diving training
def cwf_training(message):
	keyboard_cwf = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_cwf.row('◀️ Back','⬆️Train')
	keyboard_cwf.row('🗑 Clear data','🖍 Delete last attempt')
	keyboard_cwf.row('📊 View progress')


	delete_confirm_cwf = telebot.types.InlineKeyboardMarkup()
	delete_confirm_cwf.add(telebot.types.InlineKeyboardButton(text='✅ Yes', callback_data=7))
	delete_confirm_cwf.add(telebot.types.InlineKeyboardButton(text='❌ No', callback_data=8))
	
	delete_last_cwf = telebot.types.InlineKeyboardMarkup()
	delete_last_cwf.add(telebot.types.InlineKeyboardButton(text='✅ Yes', callback_data=9))
	delete_last_cwf.add(telebot.types.InlineKeyboardButton(text='❌ No', callback_data=10))

	if message.text == '◀️ Back':
		someStep = client.send_message(message.chat.id, 'Returning to training menu...', reply_markup = keyboard_train)
		client.register_next_step_handler(someStep, get_text_Train)

	if message.text == '⬆️Train':
		someStep = client.send_message(message.chat.id, '*Enter your last freediving attempt depth.*\nFor example:  15.5 or 20', reply_markup=types.ReplyKeyboardRemove(),parse_mode="Markdown")
		client.register_next_step_handler(someStep, start_cwf)

	if message.text == '🗑 Clear data':
		client.send_message(message.chat.id,'‼️ *Are you really going to DELETE all data? *‼️', reply_markup=delete_confirm_cwf,parse_mode="Markdown")
	
	if message.text == '🖍 Delete last attempt':
		client.send_message(message.chat.id,'⚠️ *Are you really going to DELETE last freediving attempt? *⚠️', reply_markup=delete_last_cwf,parse_mode="Markdown")
	
	if message.text == '📊 View progress':
		client.send_message(message.chat.id,'Loading infographics...')	
		check_progress_cwf()
		someStep = client.send_photo(message.chat.id, photo=open('cwf.png', 'rb'),reply_markup = keyboard_cwf)
		client.register_next_step_handler(someStep, cwf_training)
		delete_cwf()



def start_cwf(message):
	keyboard_cwf_cont = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_cwf_cont.row('◀️ Back','➕ Add more attempts')

	if message.text:
		if check_cwf(message.text) != -1:#########validation
			draw_cwf(check_cwf(message.text))
			someStep = client.send_photo(message.chat.id, photo=open('cwf.png', 'rb'),reply_markup = keyboard_cwf_cont)
			client.register_next_step_handler(someStep, continue_cwf)
			delete_cwf()#####deleting previous graphic

		else:
			someStep = client.send_message(message.chat.id, '*❗️Incorrect input.Please follow recomendations.❗️*\nFor example:  15.5 or 20', reply_markup=types.ReplyKeyboardRemove(),parse_mode="Markdown")
			client.register_next_step_handler(someStep, start_cwf)

def continue_cwf(message):
	keyboard_cwf_cont = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_cwf_cont.row('◀️ Back','➕ Add more attempts')
	if message.text == '◀️ Back':
		someStep = client.send_message(message.chat.id, 'Returning to training menu...', reply_markup = keyboard_train)
		client.register_next_step_handler(someStep, get_text_Train)
	if message.text == '➕ Add more attempts':
		someStep = client.send_message(message.chat.id, '*Enter your last freediving attempt depth.*\nFor example:  15.5 or 20', reply_markup=types.ReplyKeyboardRemove(),parse_mode="Markdown")
		client.register_next_step_handler(someStep, start_cwf1)

def start_cwf1(message):
	keyboard_cwf_cont = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_cwf_cont.row('◀️ Back','➕ Add more attempts')
	if check_cwf(message.text) != -1:#########validation
			draw_cwf(check_cwf(message.text))
			someStep = client.send_photo(message.chat.id, photo=open('cwf.png', 'rb'),reply_markup = keyboard_cwf_cont)
			client.register_next_step_handler(someStep, continue_cwf)
			delete_cwf()#####deleting previous graphic
			
	else:
		someStep = client.send_message(message.chat.id, '*❗️Incorrect input.Please follow recomendations.❗️*\nFor example:  2:32', reply_markup=types.ReplyKeyboardRemove(),parse_mode="Markdown")
		client.register_next_step_handler(someStep, start_cwf1)



######start dynamic training
def dynamic_training(message):
	keyboard_dynamic = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_dynamic.row('◀️ Back','⬆️Train')
	if message.text == '◀️ Back':
		someStep = client.send_message(message.chat.id, 'Returning to training menu...', reply_markup = keyboard_train)
		client.register_next_step_handler(someStep, get_text_Train)
		


######start apnea_training 
def apnea_training(message):
	keyboard_apnoe = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_apnoe.row('◀️ Back','⬆️Train')
	keyboard_apnoe.row('🗑 Clear data','🖍 Delete last attempt')
	keyboard_apnoe.row('📊 View progress')


	delete_confirm = telebot.types.InlineKeyboardMarkup()
	delete_confirm.add(telebot.types.InlineKeyboardButton(text='✅ Yes', callback_data=3))
	delete_confirm.add(telebot.types.InlineKeyboardButton(text='❌ No', callback_data=4))
	
	delete_last = telebot.types.InlineKeyboardMarkup()
	delete_last.add(telebot.types.InlineKeyboardButton(text='✅ Yes', callback_data=5))
	delete_last.add(telebot.types.InlineKeyboardButton(text='❌ No', callback_data=6))

	if message.text == '◀️ Back':
		someStep = client.send_message(message.chat.id, 'Returning to training menu...', reply_markup = keyboard_train)
		client.register_next_step_handler(someStep, get_text_Train)
	if message.text == '⬆️Train':
		someStep = client.send_message(message.chat.id, '*Enter your last apnea attempt time.*\nFor example:  2:32', reply_markup=types.ReplyKeyboardRemove(),parse_mode="Markdown")
		client.register_next_step_handler(someStep, start_apnea)
	if message.text == '🗑 Clear data':
		client.send_message(message.chat.id,'‼️ *Are you really going to DELETE all data? *‼️', reply_markup=delete_confirm,parse_mode="Markdown")
	if message.text == '🖍 Delete last attempt':
		client.send_message(message.chat.id,'⚠️ *Are you really going to DELETE last breathhold attempt? *⚠️', reply_markup=delete_last,parse_mode="Markdown")
	if message.text == '📊 View progress':
		client.send_message(message.chat.id,'Loading infographics...')	
		check_progress()
		someStep = client.send_photo(message.chat.id, photo=open('plot.png', 'rb'),reply_markup = keyboard_apnoe)
		client.register_next_step_handler(someStep, apnea_training)
		delete_graphic()



#########Enter your time        
def start_apnea(message):
	keyboard_apnoe_cont = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_apnoe_cont.row('◀️ Back','➕ Add more attempts')
	if message.text:
		if check_value_return_data(message.text) != -1:#########validation
			draw_apnea(check_value_return_data(message.text))
			someStep = client.send_photo(message.chat.id, photo=open('plot.png', 'rb'),reply_markup = keyboard_apnoe_cont)
			client.register_next_step_handler(someStep, continue_apnea)
			delete_graphic()#####deleting previous graphic

		else:
			someStep = client.send_message(message.chat.id, '*❗️Incorrect input.Please follow recomendations.❗️*\nFor example:  2:32', reply_markup=types.ReplyKeyboardRemove(),parse_mode="Markdown")
			client.register_next_step_handler(someStep, start_apnea)


########Add more attempts
def continue_apnea(message):
	keyboard_apnoe_cont = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_apnoe_cont.row('◀️ Back','➕ Add more attempts')
	if message.text == '◀️ Back':
		someStep = client.send_message(message.chat.id, 'Returning to training menu...', reply_markup = keyboard_train)
		client.register_next_step_handler(someStep, get_text_Train)
	if message.text == '➕ Add more attempts':
		someStep = client.send_message(message.chat.id, '*Enter your last apnea attempt time.*\nFor example:  2:32', reply_markup=types.ReplyKeyboardRemove(),parse_mode="Markdown")
		client.register_next_step_handler(someStep, start_apnea1)
		

######### Actually process of entering new data
def start_apnea1(message):
	keyboard_apnoe_cont = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_apnoe_cont.row('◀️ Back','➕ Add more attempts')
	if check_value_return_data(message.text) != -1:#########validation
			draw_apnea(check_value_return_data(message.text))
			someStep = client.send_photo(message.chat.id, photo=open('plot.png', 'rb'),reply_markup = keyboard_apnoe_cont)
			client.register_next_step_handler(someStep, continue_apnea)
			delete_graphic()#####deleting previous graphic
			
	else:
		someStep = client.send_message(message.chat.id, '*❗️Incorrect input.Please follow recomendations.❗️*\nFor example:  2:32', reply_markup=types.ReplyKeyboardRemove(),parse_mode="Markdown")
		client.register_next_step_handler(someStep, start_apnea1)



@client.callback_query_handler(func=lambda call: True)
def query_handler(call):

	keyboard_apnoe = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_apnoe.row('◀️ Back','⬆️Train')
	keyboard_apnoe.row('🗑 Clear data','🖍 Delete last attempt')
	keyboard_apnoe.row('📊 View progress')


	keyboard_cwf = types.ReplyKeyboardMarkup(one_time_keyboard=True) 
	keyboard_cwf.row('◀️ Back','⬆️Train')
	keyboard_cwf.row('🗑 Clear data','🖍 Delete last attempt')
	keyboard_cwf.row('📊 View progress')

	answer = ''
	if call.data == '3':
		answer = '🗑 Data cleared!'
		clear_file()
		someStep = client.send_message(call.message.chat.id, answer,reply_markup = keyboard_apnoe)
		client.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
		client.register_next_step_handler(someStep, apnea_training)
		
	elif call.data == '4':
		answer = 'Cancel!'
		someStep = client.send_message(call.message.chat.id, answer,reply_markup = keyboard_apnoe)
		client.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
		client.register_next_step_handler(someStep, apnea_training)

	answer1 = ''
	if call.data == '5':
		answer1 = '🗑 Last attempt cleared!'
		delete_last_string()
		someStep = client.send_message(call.message.chat.id, answer1,reply_markup = keyboard_apnoe)
		client.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
		client.register_next_step_handler(someStep, apnea_training)
		
	elif call.data == '6':
		answer1 = 'Cancel!'
		someStep = client.send_message(call.message.chat.id, answer1,reply_markup = keyboard_apnoe)
		client.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
		client.register_next_step_handler(someStep, apnea_training)

	answer2 = ''
	if call.data == '7':
		answer = '🗑 Data cleared!'
		clear_cwf()
		someStep = client.send_message(call.message.chat.id, answer,reply_markup = keyboard_cwf)
		client.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
		client.register_next_step_handler(someStep, cwf_training)
		
	elif call.data == '8':
		answer = 'Cancel!'
		someStep = client.send_message(call.message.chat.id, answer,reply_markup = keyboard_cwf)
		client.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
		client.register_next_step_handler(someStep, cwf_training)

	answer3 = ''
	if call.data == '9':
		answer1 = '🗑 Last attempt cleared!'
		delete_last_string_cwf()
		someStep = client.send_message(call.message.chat.id, answer1,reply_markup = keyboard_cwf)
		client.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
		client.register_next_step_handler(someStep, cwf_training)
		
	elif call.data == '10':
		answer1 = 'Cancel!'
		someStep = client.send_message(call.message.chat.id, answer1,reply_markup = keyboard_cwf)
		client.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
		client.register_next_step_handler(someStep, cwf_training)
	

client.polling(none_stop=True)