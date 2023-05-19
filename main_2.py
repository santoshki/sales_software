import wx


########################################################################
class MyPanel(wx.Panel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        self.number_of_buttons = 0
        self.number_of_txt_fields = 0
        self.frame = parent

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        controlSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.widgetSizer = wx.BoxSizer(wx.VERTICAL)

        self.addButton = wx.Button(self, label="Add")
        self.addButton.Bind(wx.EVT_BUTTON, self.onAddWidget)
        controlSizer.Add(self.addButton, 0, wx.CENTER | wx.ALL, 5)

        self.removeButton = wx.Button(self, label="Remove")
        self.removeButton.Bind(wx.EVT_BUTTON, self.onRemoveWidget)
        controlSizer.Add(self.removeButton, 0, wx.CENTER | wx.ALL, 5)

        self.mainSizer.Add(controlSizer, 0, wx.CENTER)
        self.mainSizer.Add(self.widgetSizer, 0, wx.CENTER | wx.ALL, 10)

        self.SetSizer(self.mainSizer)

    # ----------------------------------------------------------------------
    def onAddWidget(self, event):
        """"""
        self.number_of_buttons += 1
        self.number_of_txt_fields += 1
        label = "Button %s" % self.number_of_buttons
        name = "button%s" % self.number_of_buttons
        new_button = wx.Button(self, label=label, name=name)
        txt_field = wx.TextCtrl(self)
        txt_field.SetLabel("text field_" + str(self.number_of_txt_fields))
        value = txt_field.Label
        new_button.Bind(wx.EVT_BUTTON, lambda evt: self.on_click(evt, value))
        self.widgetSizer.Add(new_button, 0, wx.ALL, 5)
        self.widgetSizer.Add(txt_field, 10, wx.ALL, 10)
        self.frame.fSizer.Layout()
        self.frame.Fit()

    def on_click(self, event, value):
        print("Button added", value)

    # ----------------------------------------------------------------------
    def onRemoveWidget(self, event):
        if self.widgetSizer.GetChildren():
            print("no. of children:", self.widgetSizer.GetChildren())
            print("number of buttons currently present:", self.number_of_buttons)
            sizer_item_button = self.widgetSizer.GetItem(self.number_of_buttons - 1)
            sizer_item_textfield = self.widgetSizer.GetItem(self.number_of_txt_fields - 1)
            widget_button = sizer_item_button.GetWindow()
            widget_textfield = sizer_item_textfield.GetWindow()
            self.widgetSizer.Hide(widget_button)
            self.widgetSizer.Hide(widget_textfield)
            widget_button.Destroy()
            widget_textfield.Destroy()
            self.number_of_buttons -= 1
            self.number_of_txt_fields -= 1
            self.frame.fSizer.Layout()
            self.frame.Fit()


########################################################################
class MyFrame(wx.Frame):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="Add / Remove Buttons")
        self.fSizer = wx.BoxSizer(wx.VERTICAL)
        panel = MyPanel(self)
        self.fSizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(self.fSizer)
        self.Fit()
        self.Show()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()