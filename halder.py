ft.Container(
                    content=ft.Row([
                        ft.TextField(hint_text='Message..',border_radius=30,border=None,width=deviceWidth-15,adaptive=True,
                                     prefix=ft.IconButton(icon=ft.icons.ATTACH_FILE,icon_color='white'),
                                     suffix=ft.IconButton(icon=ft.icons.SEND,icon_color='green',),
                                     ),
                        
                    ],spacing=None,width=deviceWidth,height=60,
                                   ),width=deviceWidth,
                ),

