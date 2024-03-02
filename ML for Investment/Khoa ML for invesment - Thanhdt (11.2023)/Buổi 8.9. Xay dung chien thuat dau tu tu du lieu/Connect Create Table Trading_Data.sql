USE [Cole]
GO

/****** Object:  Table [dbo].[Trading_Data]    Script Date: 11/27/2023 11:03:09 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Trading_Data](
	[DateTime] [datetime] NULL,
	[Open] [float] NULL,
	[High] [float] NULL,
	[Low] [float] NULL,
	[Close] [float] NULL,
	[Volume] [float] NULL
) ON [PRIMARY]
GO


