button_obj = hass.states.get('sensor.tvroom_switch') 
button = button_obj.state 
if button == '1_click': 
  hass.services.call('script', 'turn_on', { "entity_id" : 'script.tvroom_button_1' }) 
elif button == '2_click': 
  hass.services.call('script', 'turn_on', { "entity_id" : 'script.tvroom_button_2' }) 
elif button == '3_click': 
  hass.services.call('script', 'turn_on', { "entity_id" : 'script.tvroom_button_3' }) 
elif button == '4_click': 
  hass.services.call('script', 'turn_on', { "entity_id" : 'script.tvroom_button_4' }) 
