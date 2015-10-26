/*
    Turtlebox

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

package lu.fisch.turtle.elements;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Point;

/**
 *
 * @author robertfisch
 */
public abstract class Element
{
    Point from;
    Point to;
    Color color = Color.BLACK;

    public Element(Point from, Point to)
    {
        this.from=from;
        this.to=to;
    }

    public Element(Point from, Point to, Color color)
    {
        this.from=from;
        this.to=to;
        this.color=color;
    }


    public abstract void draw(Graphics2D graphics);

}
