GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE IF EXISTS [dbo].Admins
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Admins')
BEGIN
CREATE TABLE [dbo].[Admins](
		[Username] [nvarchar](255) NOT NULL,
		[Key] [nvarchar](255) NOT NULL,
		PRIMARY KEY (Username),
	) ON [PRIMARY]
END
GO

DROP TABLE IF EXISTS [dbo].Signatures
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Signatures')
BEGIN
CREATE TABLE [dbo].[Signatures](
		[PrimaryKey] [nvarchar](255) NOT NULL,
		InstallCount int NOT NULL,
		InstallLimit int NOT NULL,
		UnlimitedInstalls BIT NOT NULL,
		PRIMARY KEY (PrimaryKey),
	) ON [PRIMARY]
END
GO

DROP TABLE IF EXISTS [dbo].Users
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Users')
BEGIN
CREATE TABLE [dbo].[Users](
		[Signature] int NOT NULL,
		UserID int IDENTITY(1,1) NOT NULL,
		[Name] [nvarchar](255) NOT NULL,
		Email [nvarchar](255) NOT NULL,
		Company [nvarchar](255) NOT NULL,
		InstallDateTime DATETIME NOT NULL,
		-- PRIMARY KEY ([Signature]), -- this is what they use in their made_db.py file... Not sure why they don't use a foreign key.
		PRIMARY KEY (UserID),
		FOREIGN KEY ([Signature]) REFERENCES dbo.Signatures(PrimaryKey) ON DELETE CASCADE
	) ON [PRIMARY]
END
GO

DROP TABLE IF EXISTS [dbo].Teams
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Teams')
BEGIN
CREATE TABLE [dbo].[Teams](
		[TeamID] [int] IDENTITY(1,1) NOT NULL,
		[Name] [nvarchar](255) NOT NULL,
		[Description] [nvarchar](max) NULL,
		PRIMARY KEY (TeamID),
	) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY] --kinda redundant definition of where very large files go. If we had a custom file group it would matter but it's just going to the default location for now. Don't worry about this line in other words.
END
GO

DROP TABLE IF EXISTS [dbo].Coaches
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Coaches')
BEGIN
CREATE TABLE [dbo].[Coaches](
		[CoachID] [int] IDENTITY(1,1) NOT NULL,
		[Name] [nvarchar](255) NOT NULL,
		[Description] [nvarchar](max) NULL,
		[Username] nvarchar(255) NOT NULL UNIQUE,
		[Password] nvarchar(255) NOT NULL,
		PRIMARY KEY (CoachID),
	) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY] --kinda redundant definition of where very large files go. If we had a custom file group it would matter but it's just going to the default location for now. Don't worry about this line in other words.
END
GO

DROP TABLE IF EXISTS [dbo].Athletes
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Athletes')
BEGIN
CREATE TABLE [dbo].[Athletes](
		AthleteID int IDENTITY(1,1) NOT NULL,
		[Name] [nvarchar](255) NOT NULL,
		TeamID int NULL,
		[Username] nvarchar(255) NOT NULL UNIQUE,
		[Password] nvarchar(255) NOT NULL,
		PRIMARY KEY (AthleteID),
		FOREIGN KEY (TeamID) REFERENCES dbo.Teams(TeamID) ON DELETE CASCADE
	) ON [PRIMARY] --kinda redundant definition of where very large files go. If we had a custom file group it would matter but it's just going to the default location for now. Don't worry about this line in other words.
END
GO

DROP TABLE IF EXISTS [dbo].CoachesTeams
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'CoachesTeams')
BEGIN
CREATE TABLE [dbo].[CoachesTeams](
		[CoachID] int NOT NULL,
		[TeamID] int NOT NULL,
		FOREIGN KEY (CoachID) REFERENCES dbo.Coaches(CoachID) ON DELETE CASCADE,
		FOREIGN KEY (TeamID) REFERENCES dbo.Teams(TeamID) ON DELETE CASCADE,
		PRIMARY KEY (CoachID, TeamID),
	) ON [PRIMARY]
END
GO

DROP TABLE IF EXISTS [dbo].Events
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Events')
BEGIN
CREATE TABLE [dbo].[Events](
		[EventID] [int] IDENTITY(1,1) NOT NULL,
		[Name] [nvarchar](255) NOT NULL,
		[Date] [nvarchar](255) NOT NULL,
		TeamID INT,
		PRIMARY KEY (EventID),
		FOREIGN KEY (TeamID) REFERENCES dbo.teams(TeamID) ON DELETE CASCADE,
	) ON [PRIMARY]
END
GO

DROP TABLE IF EXISTS [dbo].MessagesCtoA
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'MessagesCtoA')
BEGIN
CREATE TABLE [dbo].[MessagesCtoA](
		MessageID int IDENTITY(1,1) NOT NULL,
		[Subject] [nvarchar](255) NOT NULL,
		[Description] [nvarchar](255) NOT NULL,
		DateCreated DATETIME NOT NULL,
		CoachID INT,
		AthleteID INT,
		PRIMARY KEY (MessageID),
		FOREIGN KEY (CoachID) REFERENCES dbo.Coaches(CoachID) ON DELETE CASCADE,
		FOREIGN KEY (AthleteID) REFERENCES dbo.Athletes(AthleteID) ON DELETE CASCADE
	) ON [PRIMARY] --kinda redundant definition of where very large files go. If we had a custom file group it would matter but it's just going to the default location for now. Don't worry about this line in other words.
END
GO

DROP TABLE IF EXISTS [dbo].MessagesCtoT
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'MessagesCtoT')
BEGIN
CREATE TABLE [dbo].[MessagesCtoT](
		MessageID int IDENTITY(1,1) NOT NULL,
		[Subject] [nvarchar](255) NOT NULL,
		[Description] [nvarchar](255) NOT NULL,
		DateCreated DATETIME NOT NULL,
		CoachID INT,
		TeamID INT,
		PRIMARY KEY (MessageID),
		FOREIGN KEY (CoachID) REFERENCES dbo.Coaches(CoachID) ON DELETE CASCADE,
		FOREIGN KEY (TeamID) REFERENCES dbo.Teams(TeamID) ON DELETE CASCADE
	) ON [PRIMARY] --kinda redundant definition of where very large files go. If we had a custom file group it would matter but it's just going to the default location for now. Don't worry about this line in other words.
END
GO


