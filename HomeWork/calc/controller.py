import model_mult as model
import view

def button_click():
    model.init(view.get_value(), view.get_value())
    result = model.do_it()
    view.view_data(result)