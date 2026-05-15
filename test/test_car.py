from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest



def test_cart(login_in_driver):
        driver = login_in_driver


        #agregar producto al carrito
        
        driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
        
        contador_car =  driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert contador_car.text == "1" , "La cantidad de productos no se agrego correctamente"
        
        #obtener nombre del primer producto
        product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
        
        #ir al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        #obtener el nombre del producto en el carrito
        
        cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        
        #verificar el producto agregado en el carrito
        assert cart_item == product_name, "El producto agregado no coincide"
