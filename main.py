import flet as ft

def main(page: ft.Page): 
    page.padding = 0
    
     
    wv = ft.Text('WebView was the problem')
    sa = ft.Container(content=wv,)
    page.add(sa)

ft.app(main)
