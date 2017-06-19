import os
import sublime
import sublime_plugin

global LAST_ACTIVATED_VIEW

class TabJumperCommand(sublime_plugin.WindowCommand):
    views = []
    opened_views = []
    origin_active_view = []

    def run(self):
        global LAST_ACTIVATED_VIEW
        self.views = self.window.views()
        self.origin_active_view = self.window.active_view_in_group(self.window.active_group())

        if self.views:
            for view_index, view in enumerate(self.views):
                if view.file_name() == None:
                    viewName = 'Untitled'
                    viewPath = 'untitled'
                else:
                    file_path = self.window.project_data()['folders'][0]['path']
                    viewName = view.file_name()[view.file_name().rfind(os.sep) + 1:]
                    viewPath = view.file_name()[len(file_path) + 1:]

                self.opened_views.append([viewName, viewPath])

            for view_index, view in enumerate(self.views):
                if view.id() == LAST_ACTIVATED_VIEW.id():
                    selected_view = view_index
                    break;
                else:
                    selected_view = False

            self.window.show_quick_panel(self.opened_views, self.on_done, sublime.KEEP_OPEN_ON_FOCUS_LOST, selected_view, self.on_highlighted)
        else:
            self.window.status_message('No Files or Buffer Opened.')

    def on_done(self, index):
        # Panel Canceled
        if index == -1:
            self.window.status_message('TabJumper Canceld')
            self.window.focus_view(self.origin_active_view)
            self.opened_views = origin_active_view = []
        # Item Selected
        else:
            active_view = self.window.focus_view(self.views[index])
            self.opened_views = []

    def on_highlighted(self, index):
        pass

class RecordLastActivatedView(sublime_plugin.ViewEventListener):

    def on_deactivated(self):
        global LAST_ACTIVATED_VIEW
        LAST_ACTIVATED_VIEW = self.view