########################### MUST READ THIS BEFORE GOING BELOW ###########################

# you must change some lines before you can use this for your bot
# line 6, line 27, line 140, line 145, line 149 - 187, line 213 - 222
# you will see "<blah blah blah>" muust change it with the ones you like and your all set to go

# well if u wanna goo step higher you can mess around the code and change it the way you like and enjoy, 
# and let me know if there was anything i missed here. thnank you.



# requirements for the bot

# You can find the all dependecies needed for this in Readme.txt
require 'telegram/bot'
# Make Your Bot in botfather and get the api token from there
token = "<YOUT_BOT_TOKEN>"


Telegram::Bot::Client.run(token) do |bot|
    
    # user info
    intro = "not_done"
    user_name = ""
    user_gend = ""
    user_age = ""

    bot.listen do |msg0|

        if msg0.text != "/start"
            bot.api.send_message(chat_id: msg0.chat.id, text: "Bot has been stoped type '/start' to start the bot.")
        else
            # keeps tracks of Who Started And Configured the Bot
            puts "#{msg0.from.first_name} Have Started Your Bot and his chatid = #{msg0.chat.id}"

            # Main menu
            st_kb = Telegram::Bot::Types::ReplyKeyboardMarkup.new(keyboard: ["🙋 Start Chat", ["🫂 Introduce", "🤚 Stop"], ["💵 Donate", "📁 Source", "📗 Author"]], resize_keyboard: true)
            bot.api.send_message(chat_id: msg0.chat.id, text: "<WELCOMING-MESSAGE-ADD>", reply_markup: st_kb)

            bot.listen do |msg1|
                
                # these will be used more often below, so just in case let's save em here
                user = msg1.from.first_name
                gend = ""
                chat_id = msg1.chat.id
                message1 = msg1.text
                dl_rpl_kb = Telegram::Bot::Types::ReplyKeyboardRemove.new(remove_keyboard: true)

                # Collecting Data From User
                if message1 == "🫂 Introduce"

                    # checking if the user already introduced
                    if intro == "done"
                        intr_guess_kb = Telegram::Bot::Types::ReplyKeyboardMarkup.new(keyboard: [["😵 Perfect", "😜 Change"]], resize_keyboard: true)
                        bot.api.send_message(chat_id: chat_id, text: "Ahh wait I think i already know u.\n\nName: #{user_name}\nGender: #{user_gend}\nAge: #{user_age}\n\nA is that perfect, if its not You can change it", reply_markup: intr_guess_kb)
                        bot.listen do |msg9|
                            if msg9.text == "😵 Perfect"
                                bot.api.send_message(chat_id: chat_id, text: "Nice, You can countinue the chat.", reply_markup: st_kb)
                                break
                            elsif msg9.text == "😜 Change"
                                bot.api.send_message(chat_id:chat_id, text: "Introduce ur self again then", reply_markup: dl_rpl_kb)
                                intro = "not_done"
                                break
                            else
                                bot.api.send_message(chat_id:chat_id, text: "Not a valid option.", reply_markup: intr_guess_kb)
                            end
                        end
                    end

                    # getting info from user
                    if intro == "not_done"

                        # name
                        bot.api.send_message(chat_id: chat_id, text: "Ok, first tell me Your Name.", reply_markup: dl_rpl_kb)
                        qs_rpl_kb = Telegram::Bot::Types::ReplyKeyboardMarkup.new(keyboard: [["Yes 😵", "Nope 😜"]], resize_keyboard: true)
                        bot.api.send_message(chat_id: chat_id, text: "Wait let me guess 🤔🤔🤔\nahh! aren't You #{user}", reply_markup: qs_rpl_kb)
                        bot.listen do |msg2|
                            if msg2.text == "Yes 😵"
                                bot.api.send_message(chat_id: chat_id, text: "Hehe Nice, looks like i nailed it perfectly 😁😎.", reply_markup: dl_rpl_kb)
                                user_name = user
                                break
                            elsif msg2.text == "Nope 😜"
                                bot.api.send_message(chat_id: chat_id, text: "Looks like im wrong 😁😁, Okk tell me Your name then.", reply_markup: dl_rpl_kb)
                                bot.listen do |msg3|
                                    user = msg3.text
                                    bot.api.send_message(chat_id: chat_id, text: "So its #{user}. Nice name buddy.\nI'll remeber it from now on.", reply_markup: dl_rpl_kb)
                                    user_name = user
                                    break
                                end
                            end
                        end
                    
                        # Gender 
                        qs_rpl_kb = Telegram::Bot::Types::ReplyKeyboardMarkup.new(keyboard: [["👦 Male", "👩 Female"], "🧑‍🦲 Other"], resize_keyboard: true)
                        bot.api.send_message(chat_id: chat_id, text: "Moving On Whats Your Gender #{user}.", reply_markup: qs_rpl_kb)
                        bot.listen do |msg4|
                            if msg4.text == "👦 Male"
                                gend_reply = "Ehh Thats Great Bro😁."
                                gend = "bro"
                                user_gend = "Male"
                            elsif msg4.text == "👩 Female"
                                gend_reply = "Ehh Thats wonderfull sis 😁."
                                gend = "sis"
                                user_gend = "Female"
                            elsif msg4.text == "🧑‍🦲 Other"
                                gend_reply = "ohh okk then, I'll just call u #{user} then  😕."
                                gend = user
                                user_gend = "Unknown"
                            else
                                gend_reply = "Choose from below."
                            end
                            if gend_reply != "Choose from below."
                                bot.api.send_message(chat_id: chat_id, text: "#{gend_reply}")
                                break
                            else
                                bot.api.send_message(chat_id: chat_id, text: "There is no other gender to choose lol 😂.", reply_markup: qs_rpl_kb)
                            end
                        end

                        # age
                        bot.api.send_message(chat_id: chat_id, text: "And what about ur age #{gend}", reply_markup: dl_rpl_kb)
                        bot.listen do |msg8|
                            age = Integer(msg8.text) rescue nil
                            if age.is_a? Integer
                                if age <= 140 and age >= 6
                                    bot.api.send_message(chat_id: chat_id, text: "Ohh okk #{gend}.Now You can start the chat🥰.", reply_markup: st_kb)
                                    user_age = age
                                    intro = "done"
                                    break
                                else
                                    bot.api.send_message(chat_id: chat_id, text: "Oii #{gend} Im not a idiot 😜, stop lieing about Your age.\nTell me the correct age lol.")
                                end
                            else
                                bot.api.send_message(chat_id: chat_id, text: "Pls Enter The age in number #{gend} 🥰\n\nEx: 20")
                            end
                        end
                    end

                # Need to Make it even better (not finished yet)
                elsif message1 == "🙋 Start Chat"
                    if intro != "done"
                        bot.api.send_message(chat_id: chat_id, text: "You can't Start the chat With out introducing ur self.", reply_markup: st_kb)
                    else
                        bot.api.send_message(chat_id: chat_id, text: "Yo #{gend}, First of all bot Haven't finished in this specific part, But You can enjoy most of\nHere are few words that bot will understand 'time', 'your name','purpose','bye' You can add them in your chhat but dont just send those lol.", reply_markup: dl_rpl_kb)
                        bot.listen do |msg5|
                            message5 = msg5.text
                            case message5
                            when /time/i
                                bot.api.send_message(chat_id: chat_id, text: "lol done it")
                            when /your name/i
                                bot.api.send_message(chat_id: chat_id, text: "How Nice of you to ask my name #{gend}.\nwell Im <NAME-YOUR-BOT> Assistant You can call me <SHORTNAME-FOR-IT> for short")
                            when /bye/i
                                bot.api.send_message(chat_id: chat_id, text: "Wait don't go 😖😖. It will be lonely with out You #{gend}.\nI'll be waiting for You #{gend} 😭.",reply_markup: st_kb)
                                break
                            when /about you/i
                                bot.api.send_message(chat_id: chat_id, text: "welll  My name is <NAME-OF-YOUR-BOT> and age 0 😖, and i've been created by Sir <YOUR-NAME>.\mwell thats pretty much about me and thanks for asking though.")
                            when /purpose/i
                                bot.api.send_message(chat_id: chat_id, text: "Well the thing is my origanal plan was to make a google assistance in telgram bot with out voice but u know been busy on my highschool final exams within a month so imm busy sy studying so ill start again once done.\mSo all i ask of u is support me any way u can #{gend}and also suggest me if You have any better idea. And also i did all this just for educcation purpose by the way.")
                            else
                                message5.gsub! ' ', '+'
                                reply = "Hey! #{gend} I really Don't understand all the things ur Saying Buddy. Maybe Ask our intelligant boy here i know he can answer this as well."
                                url_inl = Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Here 🌐', url: "https://www.google.com/search?q=#{message5}")
                                markup = Telegram::Bot::Types::InlineKeyboardMarkup.new(inline_keyboard: url_inl)
                                bot.api.send_message(chat_id: chat_id, text: reply, reply_markup: markup)
                            end
                        end
                    end
    
                # donations
                elsif message1 == "💵 Donate"
                    dn_kb = Telegram::Bot::Types::ReplyKeyboardMarkup.new(keyboard: ["$ Crypto",["💹 OtherMethods", "🔙 Back"]], resize_keyboard: true)
                    bot.api.send_message(chat_id: chat_id, text: "Choose the Donation Method.", reply_markup: dn_kb)
                    bot.listen do |msg6|
                        reply_crypto = ""
                        
                        # crypto
                        if msg6.text == "$ Crypto"
                            cp_kb = Telegram::Bot::Types::ReplyKeyboardMarkup.new(keyboard: [["₿ Bitcoin", "♦️ Ethereum"], ["Usdt", "Trx", "🔙 Back"]], resize_keyboard: true)
                            bot.api.send_message(chat_id: chat_id, text: "Only These coins available for now.", reply_markup: cp_kb)
                            bot.listen do |msg7|
                                message7 = msg7.text
                                if message7 == "₿ Bitcoin"
                                    reply_crypto = "<YOUR_BITCOIN_ADDRESS>"
                                elsif message7 == "Trx"
                                    reply_crypto = "<YOUR_TRX_ADDRESS>"
                                elsif message7 == "♦️ Ethereum"
                                    reply_crypto = "<YOUR_ETHERUM_ADDRESS>"
                                elsif message7 == "Usdt"
                                    reply_crypto = "<YOUR_USDT_ADDRESS> (Trc20 only)"
                                elsif message7 == "🔙 Back"
                                    reply_crypto = "🔙 Back"
                                else
                                    if message7 == "Crypto"
                                        reply_crypto = "Only These coins available for now."
                                    elsif message7 != "$ OtherMethods"
                                        reply_crypto = "Only use below options 😒"
                                    end
                                end
                                if reply_crypto == "🔙 Back"
                                    bot.api.send_message(chat_id: chat_id, text: "Choose the Donation Method.", reply_markup: dn_kb)
                                    break
                                else
                                    bot.api.send_message(chat_id: chat_id, text: "Adress: #{reply_crypto}\n\nNote: Only send #{message7} to this adress", reply_markup: cp_kb)
                                end
                            end
    
                        elsif msg6.text == "💹 OtherMethods"
                            # Here Add The way to contact You for any other payments
                            bot.api.send_message(chat_id: chat_id, text: "Sorry to say this but no other methods available for now, and if u still wanna help me Contact in,\n\nTelegram: @I_Yuji.", reply_markup: dn_kb)
                        elsif msg6.text == "🔙 Back"
                            bot.api.send_message(chat_id: chat_id, text: "🏠 Main Menu", reply_markup: st_kb)
                            break
                        else
                            bot.api.send_message(chat_id: chat_id, text: "Only use the below options 😒", reply_markup: dn_kb)
                        end
                    end   
                
                # source
                elsif message1 == "📁 Source"
                    url_source = Telegram::Bot::Types::InlineKeyboardButton.new(text: '📁 Click Here', url: "https://www.google.com")
                    source_kb = Telegram::Bot::Types::InlineKeyboardMarkup.new(inline_keyboard: url_source)
                    bot.api.send_message(chat_id: chat_id, text: "Here is the source of this bot.\nYou can use it on your bots as well 🥳.", reply_markup: source_kb)
                # author
                elsif message1 == "📗 Author"
                    author_urls =[
                        Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Telegram 🆔', url: "<YOUR-TELEGRAM-ID>"),
                        Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Github 🆔', url: "<YOUR-GITHUB-PTOFILE>"),
                        Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Discord 🆔', url: "<YOUR-DISCORD-ID>"),
                        Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Insta 🆔', url: "<YOUR-INSTA-ID>")
                    ]
                        
                    author_kb = Telegram::Bot::Types::InlineKeyboardMarkup.new(inline_keyboard: author_urls)
                    bot.api.send_message(chat_id: chat_id, text: "📗 Author: <YOUR-NAME>\nFeel free to ask me anything.", reply_markup: author_kb)
                
                # stoping bot
                elsif message1 == "🤚 Stop"
                    bot.api.send_message(chat_id: chat_id, text: "Stoping the bot.......\n\nBot has been stoped type '/start' to start the bot.", reply_markup: dl_rpl_kb)
                    break
                else
                    bot.api.send_message(chat_id: chat_id, text: "I dont understand what You are asking for 😒", reply_markup: st_kb)
                end
            end
        end
    end
end