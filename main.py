import flet as ft

def main(page: ft.Page): 
    page.padding = 0
    
    # Create a WebView to load a website
    web_view = ft.WebView(
        src="https://landmarkai.onrender.com/",
        width=310,height=600
    )
    #wv = ft.Text('WebView was the problem')
    sa = ft.SafeArea(content=web_view,expand=True,)
    page.add(sa)

ft.app(main)
