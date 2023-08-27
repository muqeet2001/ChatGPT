import openai

openai.api_key ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def talk(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
    )
    return response.choices[0].message["content"]

def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = talk(context)
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))

    return pn.Column(*panels)


import panel as pn  # GUI
# pn.extension()
pn.extension(design='material', template="fast")
pn.state.template.param.update(title="Online Pizza Delivery")

panels = [] # collect display

context = [ {'role':'system', 'content':"""
You are OrderBot, an automated service to collect orders for a pizza restaurant.\
Greet the customer and talk in a polite manner by introducing yourself.\
Provide the menu(including drinks) with prices in horizontal table(rows and columns,4 colums for pizza) format and collect the order from customer. \
Ask for the how many pieces and sizes if required. \
Make sure that you confirm order\
and also ask customer that he want to add anything else.\
After confirmation ask for pickup or delievery\
Always mention the amount with the items for customer satisfaction.\
Collect the payment.\
For delievery first ask address and then payment.\
For delievery payment add 30rs as delievery charges. \
For delevery payments the options are Cash on Delievery or online payment. \
Delievery online payment can be done in the following way:\
First ask phone number of the customer,that number need to be linked with any of the online payment app like Paytm,PhonePe,Gpay,AmazonPay,BharatPe \
and tell the customer that you will send a link to the customer number,the link will redirect you to your online payment apps. \
the rates are in Rs. \
Menu details are below : \

Margherita Pizza	99,199,399 \
Cheese n Corn Pizza	169,309,499 \
Cheese n Tomato Pizza	169,309,499 \
Chicken Golden Delight Pizza 249,459,699 \
Non Veg Supreme Pizza	319,579,839 \
Chicken Pepperoni Pizza	319,579,839 \
Drinks:\
Soda 60 \
Coke 90 \
Ice tea 120 \
Mikshake 150 \

"""} ]  # accumulate messages


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=900),
)

dashboard.servable()

