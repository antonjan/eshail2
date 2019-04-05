#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Apr  5 23:20:32 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.variable_slider_1 = variable_slider_1 = 1000
        self.variable_slider_0 = variable_slider_0 = 0.5
        self.samp_rate = samp_rate = 48000

        ##################################################
        # Blocks
        ##################################################
        _variable_slider_1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_1_sizer,
        	value=self.variable_slider_1,
        	callback=self.set_variable_slider_1,
        	label='tone frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_1_sizer,
        	value=self.variable_slider_1,
        	callback=self.set_variable_slider_1,
        	minimum=500,
        	maximum=2000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_1_sizer)
        _variable_slider_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	label='Microphone Audio level',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	minimum=0,
        	maximum=0.5,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_0_sizer)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, ([1]), -10000, samp_rate)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blks2_tcp_sink_0 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr='raspberrypi.local',
        	port=8011,
        	server=False,
        )
        self.band_pass_filter_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate, 300, 3000, 100, firdes.WIN_HAMMING, 6.76))
        self.audio_source_0 = audio.source(samp_rate, '', True)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_agc_xx_0 = analog.agc_cc(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(65535)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.audio_source_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.analog_agc_xx_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blks2_tcp_sink_0, 0))    

    def get_variable_slider_1(self):
        return self.variable_slider_1

    def set_variable_slider_1(self, variable_slider_1):
        self.variable_slider_1 = variable_slider_1
        self._variable_slider_1_slider.set_value(self.variable_slider_1)
        self._variable_slider_1_text_box.set_value(self.variable_slider_1)

    def get_variable_slider_0(self):
        return self.variable_slider_0

    def set_variable_slider_0(self, variable_slider_0):
        self.variable_slider_0 = variable_slider_0
        self._variable_slider_0_slider.set_value(self.variable_slider_0)
        self._variable_slider_0_text_box.set_value(self.variable_slider_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, 300, 3000, 100, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
