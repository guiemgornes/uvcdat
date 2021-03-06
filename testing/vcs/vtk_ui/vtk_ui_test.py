import vtk, vcs.vtk_ui

import os, sys, time

def init():
    win = vtk.vtkRenderWindow()
    win.SetSize(100, 250)
    inter = vtk.vtkRenderWindowInteractor()
    inter.SetRenderWindow(win)
    manager = vcs.vtk_ui.manager.get_manager(inter)
    win.SetOffScreenRendering(1)
    win.AddRenderer(manager.renderer)

    return win

def generate_png(win, fnm):
    win.Render()
    out_filter = vtk.vtkWindowToImageFilter()
    out_filter.SetInput(win)
    out_filter.Update()

    png_writer = vtk.vtkPNGWriter()
    png_writer.SetFileName(fnm)
    png_writer.SetInputConnection(out_filter.GetOutputPort())
    png_writer.Write()

class vtk_ui_test(object):
    def __init__(self):
        self.win = init()
        self.inter = self.win.GetInteractor()
        self.test_file = None
        self.passed = 1

    def hover(self, x, y, duration):
        self.win.Render()
        self.inter.SetEventInformation(x, y)
        self.inter.MouseMoveEvent()
        time.sleep(duration)
        self.inter.InvokeEvent("TimerEvent")
        self.win.Render()

    def click_event(self, x, y):
        self.win.Render()
        self.inter.SetEventInformation(x, y)
        self.inter.MouseMoveEvent()
        self.inter.LeftButtonPressEvent()
        self.inter.LeftButtonReleaseEvent()

    def do_test(self):
        raise NotImplementedError("Implement do_test to execute a test.")

    def test(self):
        self.do_test()

        if self.test_file is not None:
            generate_png(self.win, self.test_file)
            if len(sys.argv) >= 2:
                src=sys.argv[1]
                pth = os.path.join(os.path.dirname(__file__),"../..")
                sys.path.append(pth)
                import checkimage
                print "fnm:", self.test_file
                print "src:", src
                self.passed = checkimage.check_result_image(self.test_file, src, checkimage.defaultThreshold)

        print sys.argv[0], "passed" if self.passed == 0 else "failed"
        sys.exit(self.passed)
