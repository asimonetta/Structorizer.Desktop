/*
    This file is part of Structorizer.

    Structorizer is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Structorizer is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

 ***********************************************************************

    KSH Source Code Generator

    Copyright (C) 2008 Jan Peter Klippel

    This file has been released under the terms of the GNU Lesser General
    Public License as published by the Free Software Foundation.

    http://www.gnu.org/licenses/lgpl.html

 */

package lu.fisch.structorizer.generators;

/******************************************************************************************************
 *
 *      Author:         Jan Peter Klippel
 *
 *      Description:    KSH Source Code Generator
 *
 ******************************************************************************************************
 *
 *      Revision List
 *
 *      Author			Date			Description
 *      ------                  ----			-----------
 *      Jan Peter Klippel       2008.04.11              First Issue
 *	Bob Fisch		2008.04.12              Added "Fields" section for generator to be used as plugin
 *      Bob Fisch               2011.11.07              Fixed an issue while doing replacements
 *
 ******************************************************************************************************
 *
 *      Comment:		LGPL license (http://www.gnu.org/licenses/lgpl.html).
 *
 ******************************************************************************************************///


import lu.fisch.structorizer.elements.Alternative;
import lu.fisch.structorizer.elements.Call;
import lu.fisch.structorizer.elements.Case;
import lu.fisch.structorizer.elements.Element;
import lu.fisch.structorizer.elements.For;
import lu.fisch.structorizer.elements.Forever;
import lu.fisch.structorizer.elements.Instruction;
import lu.fisch.structorizer.elements.Jump;
import lu.fisch.structorizer.elements.Repeat;
import lu.fisch.structorizer.elements.Root;
import lu.fisch.structorizer.elements.Subqueue;
import lu.fisch.structorizer.elements.While;
import lu.fisch.structorizer.parsers.D7Parser;
import lu.fisch.utils.BString;
import lu.fisch.utils.StringList;


public class KSHGenerator extends Generator {

	/************ Fields ***********************/
	protected String getDialogTitle()
	{
		return "Export KSH Code ...";
	}
	
	protected String getFileDescription()
	{
		return "KSH Source Code";
	}
	
	protected String getIndent()
	{
		return " ";
	}
	
	protected String[] getFileExtensions()
	{
		String[] exts = {"ksh", "sh"};
		return exts;
	}
	
	/************ Code Generation **************/
	
	private String transform(String _input)
	{
	
		_input=BString.replace(_input, " <- ", "=");
		_input=BString.replace(_input, "<- ", "=");
		_input=BString.replace(_input, " <-", "=");
		_input=BString.replace(_input, "<-", "=");
                
            StringList empty = new StringList();
            empty.addByLength(D7Parser.preAlt);
            empty.addByLength(D7Parser.postAlt);
            empty.addByLength(D7Parser.preCase);
            empty.addByLength(D7Parser.postCase);
            empty.addByLength(D7Parser.preFor);
            empty.addByLength(D7Parser.postFor);
            empty.addByLength(D7Parser.preWhile);
            empty.addByLength(D7Parser.postWhile);
            empty.addByLength(D7Parser.postRepeat);
            empty.addByLength(D7Parser.preRepeat);
            //System.out.println(empty);
            for(int i=0;i<empty.count();i++)
            {
                _input=BString.replace(_input,empty.get(i),"");
                //System.out.println(i);
            }
            if(!D7Parser.postFor.equals("")){_input=BString.replace(_input,D7Parser.postFor,"to");}

            
/*		
		if(!D7Parser.preAlt.equals("")){_input=BString.replace(_input,D7Parser.preAlt,"");}
		if(!D7Parser.postAlt.equals("")){_input=BString.replace(_input,D7Parser.postAlt,"");}
		if(!D7Parser.preCase.equals("")){_input=BString.replace(_input,D7Parser.preCase,"");}
		if(!D7Parser.postCase.equals("")){_input=BString.replace(_input,D7Parser.postCase,"");}
		if(!D7Parser.preFor.equals("")){_input=BString.replace(_input,D7Parser.preFor,"");}
		if(!D7Parser.postFor.equals("")){_input=BString.replace(_input,D7Parser.postFor,"");}
		if(!D7Parser.preWhile.equals("")){_input=BString.replace(_input,D7Parser.preWhile,"");}
		if(!D7Parser.postWhile.equals("")){_input=BString.replace(_input,D7Parser.postWhile,"");}
		if(!D7Parser.preRepeat.equals("")){_input=BString.replace(_input,D7Parser.preRepeat,"");}
		if(!D7Parser.postRepeat.equals("")){_input=BString.replace(_input,D7Parser.postRepeat,"");}
*/			
		if(!D7Parser.input.equals("")&&_input.indexOf(D7Parser.input+" ")>=0){_input=BString.replace(_input,D7Parser.input+" ","read ");}
		if(!D7Parser.output.equals("")&&_input.indexOf(D7Parser.output+" ")>=0){_input=BString.replace(_input,D7Parser.output+" ","echo ");}
		if(!D7Parser.input.equals("")&&_input.indexOf(D7Parser.input)>=0){_input=BString.replace(_input,D7Parser.input,"read ");}
		if(!D7Parser.output.equals("")&&_input.indexOf(D7Parser.output)>=0){_input=BString.replace(_input,D7Parser.output,"echo ");}
		return _input.trim();
	}
	
	protected void generateCode(Instruction _inst, String _indent) {
            if(!insertAsComment(_inst, _indent, "#"))
		for(int i=0;i<_inst.getText().count();i++)
		{
			
			code.add(_indent+transform(_inst.getText().get(i))+";");
			
		}
		
	}
	
	protected void generateCode(Alternative _alt, String _indent) {
		
		code.add("");
		code.add(_indent+"if "+BString.replace(transform(_alt.getText().getText()),"\n","").trim());
		code.add(_indent+"then");
		generateCode(_alt.qTrue,_indent+_indent.substring(0,1));
		
		if(_alt.qFalse.getSize()!=0) {
			
			code.add(_indent+"");
			code.add(_indent+"else");			
			generateCode(_alt.qFalse,_indent+_indent.substring(0,1));
			
		}
		
		code.add(_indent+"fi");
		code.add("");
		
	}
	
	protected void generateCode(Case _case, String _indent) {
		
		code.add("");
		code.add(_indent+"case "+transform(_case.getText().get(0))+" in");
		
		for(int i=0;i<_case.qs.size()-1;i++)
		{
			code.add("");
			code.add(_indent+_indent.substring(0,1)+_case.getText().get(i+1).trim()+")");
			//code.add(_indent+_indent.substring(0,1)+_indent.substring(0,1)+"begin");
			generateCode((Subqueue) _case.qs.get(i),_indent+_indent.substring(0,1)+_indent.substring(0,1)+_indent.substring(0,1));
			code.add(_indent+_indent.substring(0,1)+";;");
		}
		
		if(!_case.getText().get(_case.qs.size()).trim().equals("%"))
		{
			code.add("");
			code.add(_indent+_indent.substring(0,1)+"*)");
			generateCode((Subqueue) _case.qs.get(_case.qs.size()-1),_indent+_indent.substring(0,1)+_indent.substring(0,1));
			code.add(_indent+_indent.substring(0,1)+";;");
		}
		code.add(_indent+"esac");
		code.add("");
		
	}
	
	
	protected void generateCode(For _for, String _indent) {
		
		code.add("");
		code.add(_indent+"for "+BString.replace(BString.replace(transform(_for.getText().getText()),"=", " in "),"\n","").trim());
		code.add(_indent+"do");
		generateCode(_for.q,_indent+_indent.substring(0,1));
		code.add(_indent+"done");	
		code.add("");
		
	}
	protected void generateCode(While _while, String _indent) {
		
		code.add("");
		code.add(_indent+"while "+BString.replace(transform(_while.getText().getText()),"\n","").trim());
		code.add(_indent+"do");
		generateCode(_while.q,_indent+_indent.substring(0,1));
		code.add(_indent+"done");
		code.add("");
		
	}
	
	protected void generateCode(Repeat _repeat, String _indent) {
		
		code.add("");
		code.add(_indent+"until "+BString.replace(transform(_repeat.getText().getText()),"\n","").trim());
		code.add(_indent+"do");
		generateCode(_repeat.q,_indent+_indent.substring(0,1));
		code.add(_indent+"done");
		code.add("");
		
	}
	protected void generateCode(Forever _forever, String _indent) {
		
		code.add("");
		code.add(_indent+"while [1]");
		code.add(_indent+"do");
		generateCode(_forever.q,_indent+_indent.substring(0,1));
		code.add(_indent+"done");
		code.add("");
		
	}
	
	protected void generateCode(Call _call, String _indent) {
            if(!insertAsComment(_call, _indent, "#"))
		for(int i=0;i<_call.getText().count();i++)
		{
			code.add(_indent+transform(_call.getText().get(i))+";");
		}
		
	}
	
	protected void generateCode(Jump _jump, String _indent) {
            if(!insertAsComment(_jump, _indent, "#"))	
		for(int i=0;i<_jump.getText().count();i++)
		{
			code.add(_indent+transform(_jump.getText().get(i))+";");
		}
		
	}
	
	protected void generateCode(Subqueue _subqueue, String _indent) {
		
		// code.add(_indent+"");
		for(int i=0;i<_subqueue.children.size();i++)
		{
			generateCode((Element) _subqueue.children.get(i),_indent);
		}
		// code.add(_indent+"");
		
	}
	
	public String generateCode(Root _root, String _indent) {
		
		if( ! _root.isProgram ) {
			code.add(_root.getText().get(0)+" () {");
		} else {
				
			code.add("#!/usr/bin/ksh");
			code.add("");
			
		}
		
		code.add("# generated by structorizer");
		code.add("");
		code.add("// declare your variables here");
		code.add("");
		generateCode(_root.children,_indent);
		
		if( ! _root.isProgram ) {
			code.add("}");
		}
		
		return code.getText();
		
	}
	
}


