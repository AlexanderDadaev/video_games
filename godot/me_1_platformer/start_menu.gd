#start_menu.gd
extends Control



func _on_start_game_button_pressed():
	get_tree().change_scene("res://World.tscn")
	
func _on_quit_game_button_pressed():
	get_tree().quit()
