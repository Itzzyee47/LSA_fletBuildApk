import flet as ft

def main(page: ft.Page): 
    page.padding = 0
    
     
    wv = ft.WebView(
        "https://landmarkai.onrender.com/",
        expand=True,
    )
    sa = ft.SafeArea(content=wv,)
    page.add(sa,)

ft.app(main)
