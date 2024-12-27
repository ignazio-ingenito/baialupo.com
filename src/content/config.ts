import { z, defineCollection } from 'astro:content'

const avio = defineCollection({
	type: 'content',
	schema: z.object({
		title: z.string(),
		category: z.string(),
		featured: z.number().optional().default(0),
		image: z.string().optional(),
		created: z.coerce.date(),
		updated: z.coerce.date(),
		created_by: z.string().optional().default("Ignazio"),
	}),
})

const gallery = defineCollection({
	type: "data",
	schema: z.object({
		title: z.string(),
		cover: z.string(),
		created: z.coerce.date(),
		updated: z.coerce.date(),
		files: z.array(z.string()).default([])
	}),
})

const market = defineCollection({
	type: 'content',
	schema: z.object({
		id: z.number(),
		title: z.string(),
		description: z.string(),
		featured: z.number().optional().default(0),
		image: z.string().optional(),
		created: z.coerce.date(),
		updated: z.coerce.date(),
		created_by: z.string().optional().default("Ignazio"),
	})
})

const meteo = defineCollection({
	type: 'content',
	schema: z.object({
		title: z.string().optional(),
		pics: z.array(z.string()),
	})
})

const posts = defineCollection({
	type: 'content',
	schema: z.object({
		id: z.number(),
		title: z.string(),
		description: z.string().optional(),
		category: z.string(),
		featured: z.number().optional().default(0),
		cover: z.string().optional(),
		created: z.coerce.date(),
		updated: z.coerce.date(),
		created_by: z.string().optional().default("Ignazio"),
	}),
})

const privacy = defineCollection({
	type: 'content',
	schema: z.object({
		id: z.number(),
		title: z.string(),
		description: z.string().optional(),
		category: z.string(),
		featured: z.number().optional().default(0),
		cover: z.string().optional(),
		created: z.coerce.date(),
		updated: z.coerce.date(),
		created_by: z.string().optional().default("Ignazio"),
	}),
})

export const collections = {
	avio,
	gallery,
	meteo,
	market,
	posts,
	privacy,
}
