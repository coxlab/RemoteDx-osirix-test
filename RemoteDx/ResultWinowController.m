//
//  ResultWinowController.m
//  RemoteDx
//
//  Created by David Cox on 9/10/17.
//
//

#import "ResultWindowController.h"

@implementation ResultWindowController

- (void)awakeFromNib
{
    NSLog( @"Nib loaded!");
}

- (id) init
{
    self = [super initWithWindowNibName:@"ResultWindow"];
    
    
    [[self window] setDelegate:self];   //In order to receive the windowWillClose notification!
    
//    [self fetch];
    
    return self;
}

- (void)windowWillClose:(NSNotification *)notification
{
    NSLog(@"Window will close.... and release his memory...");
    
    [self autorelease];
}

- (void) dealloc
{
    NSLog(@"My window is deallocating a pointer");
    
    [super dealloc];
}

- (void) fetch
{
    [[web mainFrame] loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:@"http://cnn.com"]]];
}

- (void) loadContent:(NSString *)content
{
    NSLog(@"Here");
    NSLog(content);
    
    [[web mainFrame] loadHTMLString:content baseURL:[NSURL URLWithString:@"http://deep.health/"]];
}

@end
