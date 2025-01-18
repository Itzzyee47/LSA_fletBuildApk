import flet as ft
from contacts import *

deviceWidth = 360
deviceHeight = 700

def main(page: ft.Page):
    page.title= 'WhatsClone'
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 360
    page.window_height = 700  
    page.window_max_height = 700
    page.window_maximizable = False
    page.padding = 0
        
        
    def ChangeTheme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.update()
    
            
    def changeTab(e):
        t.selected_index = BTN.selected_index
        page.update()
        
    def changeBTN(e):
        BTN.selected_index = t.selected_index
        page.update()
    
    def sumation(e):
        f1 = int(fn.value)
        f2 = int(fs.value)
        result = f1 + f2
        s.value = str('Your sum is: '+ str(result))
        
        page.update()
        
    def view_pop(view):
        page.views.pop()
        page.go(page.route)
        page.update()
        
    
    page.window_always_on_top = True
    
 
    g = ft.Text('Calculator',style=ft.TextStyle(size=30,weight=ft.FontWeight.BOLD,decoration=ft.TextDecoration(1)))
    fn = ft.TextField(border_width=1, label='Frist Number')
    fs = ft.TextField(border_width=1, label='Second Number')
    space = ft.Container(height=10)
    s = ft.Text('You sum is: ', size=20)
    sumBtn = ft.ElevatedButton(text='Sum',on_click=sumation, height=40)
    status = ft.Container(
        content= ft.Row(
        [
            ft.Container(
                            image_src=f'./assets/images/avatar.png',
                            height=60,
                            width=60,
                            bgcolor=ft.colors.WHITE,
                            border_radius=ft.border_radius.all(70),
                            border=ft.border.all(3,color=ft.colors.GREEN),
                            margin=ft.margin.only(left=10),
                            padding=ft.padding.all(1.0),
                            ),
            ft.Container(
                content= ft.Column(
                    [
                        ft.Text('User name',size=15,weight=ft.FontWeight.W_500),
                        ft.Text('3:05 PM',size=10)
                    ],alignment=ft.MainAxisAlignment.SPACE_AROUND
                )
            )
        ]
    )
    )
    messageBubble = ft.Row(
        [
            ft.Container(
                            content=ft.Column( 
                                [
                                    ft.Text('Hey..',size=10,weight=ft.FontWeight.W_600),
                                    ft.Row(
                                        [
                                            ft.Text('6:44 pm',size=8,color='green'),
                                            ft.Icon(name=ft.icons.DONE_ALL,size=10, color='green')
                                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    )
                                ]
                            ),bgcolor=ft.colors.BLACK12,blur=8
                            ,padding=9,border_radius=ft.BorderRadius(0,10,10,10),width=120
                            ),
        ],alignment=ft.MainAxisAlignment.START
    )
    messageBubble2 = ft.Row(
        [
            ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text('Hello oawibdaoiwbodaiw doawidbnoaiwbndoaibw doaiwndoiabwodba owdainbwoidbaow doaiwnbdoiwdoa owdinaowdbi aowidb',size=10,weight=ft.FontWeight.W_600),
                                    ft.Row(
                                        [
                                            ft.Text('6:44 pm',size=8,color='green'),
                                            ft.Icon(name=ft.icons.DONE_ALL,size=10, color='green')
                                        ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    )
                                ]
                            ),bgcolor=ft.colors.with_opacity(0.5,ft.colors.BLUE_400), blur=8
                            ,padding=9,border_radius=ft.BorderRadius(10,0,10,10),width=230
                            ),
        ],alignment=ft.MainAxisAlignment.END
    )
    
#components....

    signInPage = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                'Log-on',size=30,weight=ft.FontWeight.BOLD,
                            ),
                            ft.TextField(
                                border=ft.InputBorder.OUTLINE,
                                label_style=ft.TextStyle(color='white'),
                                label='User name',border_radius=ft.border_radius.all(50)
                            ),
                            ft.TextField(
                                keyboard_type=ft.KeyboardType.NUMBER,
                                border=ft.InputBorder.OUTLINE,
                                label_style=ft.TextStyle(color='white'),
                                label='Phone number',prefix=ft.Text('+237')
                                ,border_radius=ft.border_radius.all(50)
                            ),
                            ft.ElevatedButton('Log-on',icon=ft.icons.LOGIN_OUTLINED,on_click= lambda e:page.go('/auth'))
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        
                    ),alignment=ft.alignment.center,padding=10,margin=15,height=450,
                    bgcolor=ft.colors.with_opacity(0.8,'green'),border_radius=ft.border_radius.all(10),
                    blur=0.9,
                )
            ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=1,
            
        ),expand=True,image_src=f'./assets/images/bg3.jpg',opacity=1,image_fit=ft.ImageFit.COVER,
    )
    
    OTPpage = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                'Authentication',size=30,weight=ft.FontWeight.BOLD,
                            ),
                            ft.Column(
                                [
                                    ft.Container(
                                        content=ft.TextField(
                                            border=ft.InputBorder.UNDERLINE,
                                            label='Enter OTP code',
                                            label_style=ft.TextStyle(color='white'),
                                            max_length=6,keyboard_type=ft.KeyboardType.NUMBER,
                                            text_align=ft.TextAlign.CENTER
                                            ),
                                        height=100,
                                    ),
                                    ft.Container(
                                        content=ft.Text('Resend code',),
                                         on_click= lambda _: print('clicked')
                                    )
                                ]
                            ),
                            ft.ElevatedButton('Submit',on_click= lambda e:page.go('/home'))
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        
                    ),alignment=ft.alignment.center,padding=10,margin=15,height=450,
                    bgcolor=ft.colors.with_opacity(0.8,'green'),border_radius=ft.border_radius.all(10),
                    blur=1,
                )
            ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=1,
            
        ),expand=True,image_src=f'./assets/images/bg3.jpg',opacity=1,image_fit=ft.ImageFit.COVER,
    )

    abar = ft.Container(
        content=ft.Row(
            [
                ft.Text('WhatzClone', size=19, weight=ft.FontWeight.W_700,expand=1),
                ft.Container(
                    content=ft.Row(
                        [
                            ft.IconButton(icon=ft.icons.WB_SUNNY_OUTLINED,on_click=ChangeTheme,),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text="Item 1",on_click=lambda _:page.go('/')),
                                    ft.PopupMenuItem(text="Item 2"),
                                    ft.PopupMenuItem(text="Item 3"), 
                                ],
                                menu_position= ft.PopupMenuPosition.UNDER
                            ),
                        ],spacing=1,
                    )
                )
            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),top=0,padding=ft.padding.only(left=10,right=20),
        height=45,width=deviceWidth,border=ft.border.only(bottom=ft.BorderSide(0.2,color=ft.colors.GREY_50)),margin= ft.Margin(left=10, top=0, right=0, bottom=0)
    )
    
    user = ft.ListTile(
            content_padding=ft.padding.only(left=10,right=10),
            leading=ft.Container(
                        image_src=f'./assets/images/avatar.png',
                    height=40,
                    width=40,
                        bgcolor=ft.colors.WHITE,
                        border_radius=ft.border_radius.all(80),
                        
                    ),
            title=ft.Text("User name",weight=ft.FontWeight.W_600),
            subtitle=ft.Text('user discription'),
            on_click= lambda _: page.go('/conversations'),
            title_alignment= ft.ListTileTitleAlignment.TITLE_HEIGHT
        )
    
    
    listCOnversations = ft.ListView([])
    
    for contact in contacts:
        listCOnversations.controls.append(
            ft.ListTile(
                content_padding=ft.padding.only(left=10,right=10),
                leading=ft.Container(
                            image_src=f'./assets/images/avatar.png',
                        height=40,
                        width=40,
                            bgcolor=ft.colors.WHITE,
                            border_radius=ft.border_radius.all(80),
                            
                        ),
                title=ft.Text(f'{contact['name']}',weight=ft.FontWeight.W_600),
                subtitle=ft.Text(f'{contact['number']}'),
                on_click= lambda _: page.go('/conversations'),
                title_alignment= ft.ListTileTitleAlignment.TITLE_HEIGHT
            )
        )
          
    
    startConversation = ft.Container(
        content= ft.Column(
            [
                ft.Text('Users on whatzClone',text_align=ft.TextAlign.CENTER,width=deviceWidth,size=13),
               listCOnversations
            ],scroll=ft.ScrollMode.HIDDEN,auto_scroll=False,spacing=0
        ),expand=1,
    )
    
    
    searchAppBar = ft.AppBar(
        
        actions=[
            ft.Container(
                content= ft.SearchBar(
                        bar_hint_text='Search name or number',
                        bar_leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click= lambda _: page.go('/home') ),
                        bar_trailing= [
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text="Item 1"),
                                    ft.PopupMenuItem(text="Item 2"),
                                ],
                                menu_position= ft.PopupMenuPosition.UNDER
                            )
                        ],width=deviceWidth-20,
                        on_change= lambda e: search(e)
                        ),alignment=ft.alignment.center,
                
            )
        ],
    )
    
    
    searchValue = searchAppBar.actions[0].content
    
    # Search algorithm
    def search(e):
        #print(f'Changing {searchValue.value}')
        searchTerm = searchValue.value
        #print(f'{listCOnversations.controls}') 
        filteredList = [item for item in contacts if searchTerm in item["name"].lower()]
        
        
        listCOnversations.controls.clear()
    
        for contact in filteredList:
            listCOnversations.controls.append(
                ft.ListTile(
                    content_padding=ft.padding.only(left=10,right=10),
                    leading=ft.Container(
                                image_src=f'./assets/images/avatar.png',
                            height=40,
                            width=40,
                                bgcolor=ft.colors.WHITE,
                                border_radius=ft.border_radius.all(80),
                                
                            ),
                    title=ft.Text(f'{contact['name']}',weight=ft.FontWeight.W_600),
                    subtitle=ft.Text(f'{contact['number']}'),
                    on_click= lambda _: page.go('/conversations'),
                    title_alignment= ft.ListTileTitleAlignment.TITLE_HEIGHT
                )
            )
            
        page.update()
            
    
    hovBtn = ft.Container(
        content=ft.IconButton(icon_color=ft.colors.GREY_900,icon=ft.icons.ADD_COMMENT,on_click= lambda _: page.go('/startConversation')),
        width=50,height=50,bottom=10,right=10,bgcolor=ft.colors.GREEN,border_radius=ft.border_radius.all(10)
    )
     
    conversationView = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Row([
                            ft.IconButton(icon=ft.icons.ARROW_BACK,on_click= lambda _: page.go('/home'),),
                            ft.Row([
                                ft.Container(
                                image_src=f'./assets/images/avatar.png',height=40,width=39,bgcolor=ft.colors.WHITE,
                                border_radius=ft.border_radius.all(90),),
                                ft.Text('userName..'),
                            ])
                            ],spacing=2
                        ),
                        ft.Row(
                            [
                                ft.IconButton(icon=ft.icons.ADD_IC_CALL_OUTLINED),
                                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(text="Item 1"),
                                        ft.PopupMenuItem(text="Item 2"),
                                        ft.PopupMenuItem(text="Item 3"),
                                    ],
                                    menu_position= ft.PopupMenuPosition.UNDER
                                ),
                            ],spacing=2
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,expand=1
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                content=ft.Column(
                                    [
                                        messageBubble2, messageBubble, messageBubble2,
                                        messageBubble, messageBubble2, messageBubble,
                                        messageBubble2, messageBubble, messageBubble,
                                        messageBubble2, messageBubble, messageBubble,messageBubble2,
                                    ],scroll=True,auto_scroll=True
                                ),width=deviceWidth,expand=9,padding=ft.padding.only(left=10,right=10)
                            ),
                            ft.Container(
                                content= ft.Row([
                                    ft.TextField(
                                        multiline=True,
                                        hint_text='Message..',border=ft.InputBorder.UNDERLINE,adaptive=True,
                                        prefix=ft.IconButton(icon=ft.icons.EMOJI_EMOTIONS,icon_color='green'),
                                        suffix=ft.IconButton(icon=ft.icons.ATTACH_FILE,icon_color='green',),
                                        fill_color=ft.colors.with_opacity(0.1,ft.colors.GREY_300),
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.SEND,
                                        bgcolor='green'
                                    )
                                ],spacing=0
                                                )
                                ,width=deviceWidth,expand=1,padding=5,blur=1
                            )
                        ],spacing=0
                    ),expand=11,image_src=f'./assets/images/bg3.jpg',image_fit=ft.ImageFit.COVER,
                    image_opacity=0.1
                )

                
                
            ],spacing=0,
        ),
        width=deviceWidth,expand=True,
        
    )  
    
    currentChats = ft.Column(
                    scroll= ft.ScrollMode.HIDDEN ,
                    controls=[],
                    spacing=1,  
                    auto_scroll= False,
                    
                )
    
    def addCurrentChats():
        for contact in contacts:
            currentChats.controls.append(
                
                    ft.ListTile(
                        content_padding=ft.padding.only(left=10,right=10),
                        leading=ft.Container(
                                    image_src=f'./assets/images/avatar.png',
                                height=50,
                                width=48,
                                    bgcolor=ft.colors.WHITE,
                                    border_radius=ft.border_radius.all(90),
                                    
                                ),
                        title=ft.Text(f'{contact["name"]}',weight=ft.FontWeight.W_600),
                        subtitle=ft.Text('message brif'),
                        trailing=ft.Text('6:41',color=ft.colors.GREEN_600),
                        
                        on_click= lambda _: page.go('/conversations')
                        
                        
                    )
                 
            )
    

    addCurrentChats()
    t = ft.Tabs(
        
        tab_alignment= ft.MainAxisAlignment.CENTER,
        selected_index=0,
        animation_duration=300,
        indicator_tab_size=False,
        indicator_thickness=0.1,
         
        
        tabs=[
            #CONVERATION TAB...................
            ft.Tab(
                
                content=ft.Container(
                    margin=1,
                    padding=0,
                    expand=1 ,
                    content=currentChats
                ),
            ),
            
            #STATUS TAB.................
            ft.Tab(
                
                content=ft.Column(
                    [
                        ft.Container(
                            content=ft.Row(
                            
                            controls=[
                                    ft.Text('Status',size=19,weight=ft.FontWeight.W_400),
                                ],
                            alignment=ft.MainAxisAlignment.START,
                            )
                            ,width=350,padding=ft.padding.only(10,0,10,0)
                        ),
                        ft.Column(
                            [
                                status,status,status,status,status,status,status,status,status,status,status,status,status,status
                            ],
                            scroll=True
                        )
                    ],scroll=True
                    ),
            ),
            
            #COMMUNITY TAB...............
            ft.Tab(
                text=None,
                adaptive=False,
                content=ft.Container(
                    
                        content=ft.Column(
                        horizontal_alignment= ft.CrossAxisAlignment.CENTER ,
                            controls=[
                            
                            g,space,
                            fn,
                            fs,
                            space,s,
                            sumBtn
                            ],
                        ), alignment=ft.alignment.center
                ),
            ),
            
            #CALLS TAB...............
            ft.Tab(
                
                content=ft.Column(
                    
                    [
                        ft.Container(
                            image_src=f'./proMale.png',
                        height=100,
                        width=100,
                            bgcolor=ft.colors.WHITE,
                            border_radius=ft.border_radius.all(90),
                            padding=ft.padding.all(1.0)
                        ),
                    ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    
                ),
                
            ),
            
        ],
        expand=7,
        on_change= changeBTN ,
    )
    
    
    
    
    BTN = ft.NavigationBar(
        indicator_color=ft.colors.GREEN,
        selected_index=0,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.CHAT_OUTLINED, label="Chats",selected_icon=ft.icons.CHAT,),
            ft.NavigationBarDestination(icon=ft.icons.UPDATE_SHARP, label="Updates"),
            ft.NavigationBarDestination(icon=ft.icons.GROUP_OUTLINED, label="Communities",),
            ft.NavigationBarDestination(
                icon=ft.icons.PHONE_OUTLINED,
                selected_icon=ft.icons.PHONE, 
                label="Calls",
            ),
        ],
        on_change= changeTab
    )
    
    stack = ft.Stack(
        [
            t,
            abar,hovBtn,
        ],alignment=ft.alignment.center,expand=True
    )
    pages = {
        '/': ft.View( "/", [signInPage,],padding=0,navigation_bar=None),
        '/auth': ft.View( "/auth", [OTPpage,],padding=0,navigation_bar=None),
        '/home': ft.View( "/home", [stack,BTN],padding=0,  ), 
        '/conversations': ft.View( "/conversations", [conversationView,],padding=0, ),
        '/startConversation': ft.View( "/startConversation", [startConversation,],padding=0,appbar=searchAppBar, navigation_bar=None ),
    }
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
            
        )
        page.update() 
        "Zyee@Chat47"
        
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main,assets_dir="assets") 
