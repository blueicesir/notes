#selenium
+ click(locator)
+ double_click(locator)
+ context_menu(locator)
+ click_at(locator,coordString)
+ double_click_at(locator,coordString,])
+ content_menu_at(locator,coordString)
+ fire_event(locator,eventName)
+ focus(locator)
+ key_press(locator,keySequence)
+ shift_key_down()
+ shift_key_up()
+ meta_key_down()
+ meta_key_up()
+ alt_key_down()
+ alt_key_up()
+ control_key_down()
+ control_key_up()
+ key_down(locator,keySequence)
+ key_up(locator,keySequence)
+ mouse_over(locator)
+ mouse_out(locator)
+ mouse_down(locator)
+ mouse_down_right(locator)
+ mouse_down_at(locator,coordString)
+ mouse_down_right(at(locator,coordString)
+ mouse_up_right(loctor)
+ mouse_up_at(locator,coordString)
+ mouse_Up_right_at(locator,coordString)
+ mouse_move(locator)
+ mouse_move_at(locator,coordString)
+ type(locator,value)
+ type_keys(locator,vlaue)
+ set_speed(value)
+ get_speed()
+ get_log()
+ check(locator) # Check a toggle-button checkbox/radio
+ uncheck(locator) # Uncheck a toggle-button (checkbox/radio)
+ select(selectLocator,optionLocator)
+ add_selection(locator,optionLocator)
+ remove_select(locator,optionLocator)
+ remove_all_selections(locator)
+ submit(formLocator)
+ open(url,ignoreResponseCode=True)
+ open_window(url,windowID)
+ select_window(windowID)
+ select_pop_up(windowID)
+ deselect_pop_up()
+ select_frame(locator)
+ get_whether_this_frame_match_frame_expression(currentFrameString,target)
+ get_whether_this_window_match_window_expression(currentWindowString,target)
+ wait_for_pop_up(windowID,timeout)
+ choose_cancel_on_next_confirmation()
+ choose_ok_on_next_confirmation()
+ answer_on_next_prompt(answer)
+ go_back()
+ refresh()
+ close()
+ is_alert_present() # 是否发生alert，这个函数永远不会产生异常
+ is_prompt_present() # 是否产生提示，就是录入文字的框
+ is_confirmation_present() # 是否产生提示
+ get_alert()
+ get_confirmation()
+ get_prompt()
+ get_location()
+ get_title()
+ get_body_text()
+ get_value(locator) # input field or anything else with a value parameter
+ get_text(locator)
+ highlight(locator) # 高亮元素
+ get_eval(script) # 执行脚本并返回
+ is_checked(locator)
+ get_table(tableCellAddress) # Gets the text from a cell of a table. The cellAddress syntax tableLocator.row,column,where row and column start at 0.
+ get_selected_labels(selectLocator)
+ get_selected_label(selectLocator)
+ get_selected_values(selectLocator)
+ get_selected_value(selectLocator)
+ get_selected_indexes(selectLocator)
+ get_selected_index(selectLocator)
+ get_selected_ids(selectLocator)
+ get_selected_id(selectLocator)
+ is_something_selected(selectLocator)
+ get_select_options(selectLocator)
+ get_attribute(attributeLocator) # attributeLocator is an element locator followed by an @ sign and then the name of the attribute, e.g. "foo@bar"
+ is_text_present(pattern) # 检查文字是否存在
+ is_element_present(locator) # 检查元素是否存在
+ is_visible(locator)
+ is_editable(locator)
+ get_all_buttons() # return the IDs of all buttons on the page
+ get_all_links()
+ get_all_fields() # return the IDs of all input fields on the page
+ get_attribute_from_all_windows(attributeName) # 返回所有窗口的指定属性
+ dragdrop(locator,movementsString)
+ set_mouse_speed(pixels) # default=10
+ get_mouse_speed()
+ drag_and_drop(locator,movementsString)
+ drag_and_drop_to_object(locatorOfObjectToBeDragged,localtorOfDrageDestinationObject)
+ window_focus()
+ window_maximize()
+ get_all_window_ids() # 返回所有窗口的ID
+ get_all_window_names() # 返回所有窗口的名称
+ get_all_window_titles() # 返回所有窗口的标题
+ get_html_source()
+ set_cursor_position(locator,position)
+ get_element_index(locator)
+ is_ordered(locator1,locator2)
+ get_element_position_left(locator)
+ get_element_position_top(loator)
+ get_element_width(locator)
+ get_element_height(locator)
+ get_cursor_position(locator)
+ get_expression(expression) # It is used to generate commands lik assertExpression and waitFromExpression
+ get_xpath_count(xpath)
+ get_css_count(css)
+ assign_id(locator,identifier)
+ allow_native_xpath(allow)
+ ignore_attributes_without_value(ignore)
+ wait_for_condition(script,timeout) # 多次运行script直到结果为真或者超时
+ set_timeout(timeout) # 等待Selenium执行动作的超时时间
+ wait_for_page_to_load(timeout) # 等待新的页面加载完成
+ wait_for_frame_to_load(frameAddress,timeout) # 等待新的frame加载完成
+ get_cookie()
+ get_cookie_by_name(name)
+ is_cookie_present(name)
+ create_cookie(nameValuePair,optionsString)
+ delete_cookie(name,optionsString)
+ delete_all_visible_cookie()
+ set_browser_log_level(logLevel)
+ run_script(script)
+ add_location_strategy(strategyName,functionDefinition)
+ capture_entrie_page_screenshot(filename,kwargs)
+ rollup(rollupName,kwargs)
+ add_script(scriptContent,scriptTagId)
+ remove_script(scriptTagId)
+ use_xpath_library(libraryName) # ajaxslt,javascript-xpath,default
+ set_context(context)
+ attach_file(fieldLocator,fileLocator) # file input (upload) field to the file listed in fileLocator
+ capture_screenshot(filename)
+ capture_screenshot_to_string()
+ captureNetworkTraffic(type) # json,xml,plain
+ capture_network_traffic(type)
+ addCustomRequestHeader(key,value)
+ add_custom_request_header(key,value)
+ shut_down_selenium_server()
+ retrieve_liast_remote_control_logs()
+ key_down_native(keycode)
+ key_up_native(keycode)
+ key_press_native(keycode)


