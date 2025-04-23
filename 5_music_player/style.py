def group_box_style():
    return """
        QGroupBox {
            background-color: #fcc324;
            font-family: Times New Roman;
            color: white;
            border-width: 2px;
            border-color: gray;
            border-style: solid;
            border-radius: 15px;
        }
    """

def progress_bar_style():
    return """
        QProgressBar {
            border: 1px solid #bbb;
            background-color: white; 
            height: 10px;
            border-radius: 6px;
        }
    """

def list_widget_style():
    return """
        QListWidget {
            background-color: #fff;
            border-radius: 10px;
            border: 3px solid blue;
        }
    """