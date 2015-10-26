/*
    Structorizer
    A little tool which you can use to create Nassi-Schneiderman Diagrams (NSD)

    Copyright (C) 2009  Bob Fisch

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or any
    later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

import javax.swing.UIManager;
import lu.fisch.structorizer.gui.Mainform;

public class Structorizer
{

	// entry point
	public static void main(String args[])
	{
                // try to load the system Look & Feel
		try
		{
			UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
		}
		catch(Exception e)
		{
			//System.out.println("Error setting native LAF: " + e);
		}

		// load the mainform
		final Mainform mainform = new Mainform();

		try
		{
			String s = new String();
                        int start = 0;
                        if(args.length>0)
                            if (args[0].equals("-open"))
                                start=1;
			for(int i=start;i<args.length;i++)
			{
				s+=args[i];
			}
			//System.out.println("Opening from shell: "+s);
			mainform.diagram.openNSD(s);
			mainform.diagram.redraw();
		}
		catch (Exception e)
		{
		}


		if(System.getProperty("os.name").toLowerCase().startsWith("mac os x"))
		{

                    System.setProperty("apple.laf.useScreenMenuBar", "true");
                    System.setProperty("apple.awt.graphics.UseQuartz", "true");

                    com.apple.eawt.Application application = com.apple.eawt.Application.getApplication();

                    try
                    {
                    application.setEnabledPreferencesMenu(true);
                    application.addApplicationListener(new com.apple.eawt.ApplicationAdapter() {
                                                                                            public void handleAbout(com.apple.eawt.ApplicationEvent e) {
                                                                                                    mainform.diagram.aboutNSD();
                                                                                                    e.setHandled(true);
                                                                                            }
                                                                                            public void handleOpenApplication(com.apple.eawt.ApplicationEvent e) {
                                                                                            }
                                                                                            public void handleOpenFile(com.apple.eawt.ApplicationEvent e) {
                                                                                                    if(e.getFilename()!=null)
                                                                                                    {
                                                                                                            mainform.diagram.openNSD(e.getFilename());
                                                                                                    }
                                                                                            }
                                                                                            public void handlePreferences(com.apple.eawt.ApplicationEvent e) {
                                                                                                    mainform.diagram.preferencesNSD();
                                                                                            }
                                                                                            public void handlePrintFile(com.apple.eawt.ApplicationEvent e) {
                                                                                                    mainform.diagram.printNSD();
                                                                                            }
                                                                                            public void handleQuit(com.apple.eawt.ApplicationEvent e) {
                                                                                                    mainform.saveToINI();
                                                                                                    mainform.dispose();
                                                                                            }
                                                                                            });
                    }
                    catch (Exception e)
                    {
                    }
                }/**/


	}
}
