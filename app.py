from ext import app
from routes import index, register, login, logout, create_product, edit_product, delete_product, about, profile



app.run(debug=True, host="0.0.0.0")
