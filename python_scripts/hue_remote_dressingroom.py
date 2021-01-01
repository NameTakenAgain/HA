button_obj = hass.states.get('sensor.dressingroom_switch') 
button = button_obj.state 
if button == '1_click_up': 
  hass.services.call('script', 'turn_on', { "entity_id" : 'script.dressingroom_button_1' }) 
elif button == '2_click_up': 
  hass.services.call('script', 'turn_on', { "entity_id" : 'script.dressingroom_button_2' }) 
elif button == '3_click_up': 
  hass.services.call('script', 'turn_on', { "entity_id" : 'script.dressingroom_button_3' }) 
elif button == '4_click_up': 
  hass.services.call('script', 'turn_on', { "entity_id" : 'script.dressingroom_button_4' }) 
