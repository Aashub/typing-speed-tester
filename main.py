from api_request import ApiClient
from userinterface import UserInterface


# request_text = ApiClient()
# typing_text = request_text.easy_text

typing_text ="T-bone pancetta quis cupidatat tongue dolore. Filet mignon nisi Filet mignon nisi pork loin, short loin drumstick pork belly ullamco sunt short ribs sirloin picanha burgdoggen commodo venison.  Consectetur exercitation Filet mignon nisi pork loin, short loin drumstick pork belly ullamco sunt short ribs sirloin picanha burgdoggen Filet mignon nisi pork loin, short loin drumstick pork belly ullamco sunt short ribs sirloin picanha burgdoggen commodo venison.  Consectetur exercitation ham hock nisi ground round Filet mignon nisi pork loin, short loin drumstick pork belly ullamco sunt short ribs sirloin picanha burgdoggen commodo venison.  Consectetur exercitation ham hock nisi ground round Filet mignon Filet mignon nisi pork loin, short loin drumstick pork belly ullamco sunt short ribs sirloin picanha burgdoggen commodo venison.  Consectetur exercitation ham hock nisi ground round kielbasa enim jowl do anim frankfurter turkey hamburger filet mignon ullamco.  Sausage chuck nulla ball tip alcatra elit ut andouille polony mollit eiusmod deserunt ground round qui shoulder.  Short ribs meatloaf veniam, reprehenderit voluptate drumstick elit sint.  Aliqua aliquip rump labore ad beef ribs.  Spare ribs aliqua pork loin, mortadella eu veniam boudin laborum pastrami Turkey short ribs do, minim commodo brisket laborum ball tip aliqua.  Anim frankfurter culpa, porchetta turkey sunt beef kielbasa chislic sausage aliquip strip steak biltong magna sirloin.  Consequat laborum meatball et.  Irure qui anim eiusmod, jowl tenderloin drumstick chicken excepteur.  Chislic tail sausage strip steak.  Incididunt ad veniam brisket et beef ribs voluptate occaecat sunt nulla pastrami duis kevin mollit. Pastrami velit consectetur quis spare ribs enim excepteur incididunt pork loin magna ham boudin leberkas.  Ut ullamco buffalo quis, flank capicola boudin meatball excepteur minim culpa.  Ut est in anim cupim officia ribeye.  Frankfurter in leberkas strip steak enim aliquip duis, ball tip tail buffalo dolore prosciutto.  Tri-tip sirloin shankle shank enim, laborum sed jowl. Rump ut filet mignon enim, nostrud alcatra ex kielbasa voluptate fugiat.  Ham hock flank irure tenderloin non ex mollit.  Shankle eu culpa officia.  Nostrud pork chop cillum, chislic doner filet mignon sausage flank magna veniam.  Nostrud mortadella aute in, adipisicing pancetta nisi corned beef quis landjaeger laboris."


ui = UserInterface()
ui.add_typing_test_screen()
ui.display_typing_text(typing_text)
ui.all_widget_button()
ui.bind("<KeyRelease>", ui.check_retrieved_text)



ui.mainloop()


